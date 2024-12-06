from utils import *


def view_university(university_code):
    """
    Fetch and display details of a university.

    Parameter:
        university_code: Code of the university. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['universities']

    result = collection.find_one({'code': university_code})
    print(result)

    closeConnection(conn)


def view_season(season_code):
    """
    Fetch and display details of a season.

    Parameter:
        season_code: Code of the season. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['seasons']

    result = collection.find_one({'code': season_code})
    print(result)

    closeConnection(conn)


def view_tournament(tournament_code):
    """
    Fetch and display details of a tournament.

    Parameter:
        tournament_code: Code of the tournament. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['tournaments']

    result = collection.find_one({'code': tournament_code})
    print(result)

    closeConnection(conn)


def view_team(team_code):
    """
    Fetch and display details of a team.

    Parameter:
        team_code: Code of the team. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['teams']

    result = collection.find_one({'code': team_code})
    print(result)

    closeConnection(conn)


def view_player(player_code):
    """
    Fetch and display details of a player.

    Parameters:
        player_code: Code of the player. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['players']

    result = collection.find_one({'code': player_code})
    print(result)

    closeConnection(conn)


def view_matches(tournament_code, team_code=None, status=None):
    """
    Finds all matches in a tournament, optionally filtering 
    by a specific team and/or match status.

    Parameters:
        tournament_code: Code of the tournament. (String)
        team_code: (Optional) Code of the team to filter matches by. (String)
        status: (Optional) Status of the match (e.g., 'Completed', 'Ongoing'). (String)
                If None, retrieves matches regardless of status.
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['matches']

    match_filter = {
        'tournament_code': tournament_code
    }
    if team_code:
        match_filter['$or'] = [
            {'team1.team_code': team_code},
            {'team2.team_code': team_code}
        ]
    if status:
        match_filter['status'] = status

    pipeline = [
        {'$match': match_filter},
        {
            '$lookup': {
                'from': 'teams',
                'localField': 'team1.team_code',
                'foreignField': 'code',
                'as': 'team1_details'
            }
        },
        {
            '$lookup': {
                'from': 'teams',
                'localField': 'team2.team_code',
                'foreignField': 'code',
                'as': 'team2_details'
            }
        },
        {
            '$unwind': {
                'path': '$team1_details',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$unwind': {
                'path': '$team2_details',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup': {
                'from': 'players',
                'localField': 'team1_details.roster',
                'foreignField': 'code',
                'as': 'team1_details.roster'
            }
        },
        {
            '$lookup': {
                'from': 'players',
                'localField': 'team2_details.roster',
                'foreignField': 'code',
                'as': 'team2_details.roster'
            }
        },
        {
            '$project': {
                '_id': 0,
                'code': 1,
                'tournament_code': 1,
                'status': 1,
                'team1': 1,
                'team2': 1,
                'team1_details.name': 1,
                'team1_details.coach': 1,
                'team1_details.roster': {
                    'first_name': 1,
                    'last_name': 1,
                    'username': 1
                },
                'team2_details.name': 1,
                'team2_details.coach': 1,
                'team2_details.roster': {
                    'first_name': 1,
                    'last_name': 1,
                    'username': 1
                }
            }
        }
    ]

    results = collection.aggregate(pipeline)

    for match in results:
        print(match)

    closeConnection(conn)


def tournamentLeaderboard(tournament_code):
    """
    View a leaderboard of a tournament based on overall_score, 
    sorted in descending order.

    Parameter:
        tournament_code: Code of the tournament. (String)
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['teams']

    results = collection.aggregate([
        {'$match': {'tournament_code': tournament_code}},
        {'$project': {'_id': 0, 'name': 1, 'overall_score': 1}},
        {'$sort': {'overall_score': -1}}
    ])

    for team in results:
        print(team)

    closeConnection(conn)


def tournamentTopFour(tournament_code):
    """
    Finds and retrieves the top 4 teams of a tournament 
    based on overall_score.

    Parameters:
        tournament_code: Code of the tournament. (String)
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['teams']

    results = collection.aggregate([
        {'$match': {'tournament_code': tournament_code}},
        {'$project': {'_id': 0, 'name': 1, 'overall_score': 1}},
        {'$sort': {'overall_score': -1}},
        {'$limit': 4}
    ])

    for team in results:
        print(team)

    closeConnection(conn)


def tournamentWinner(tournament_code):
    """
    Finds and retrieves the winner of a tournament based on 
    the highest overall_score.

    Parameters:
        tournament_code: Code of the tournament. (String)
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['teams']

    result = collection.aggregate([
        {'$match': {'tournament_code': tournament_code}},
        {'$project': {'_id': 0, 'name': 1, 'overall_score': 1}},
        {'$sort': {'overall_score': -1}},
        {'$limit': 1}
    ])

    for winner in result:
        print(winner)

    closeConnection(conn)


def seasonTournamentWinners(season_code):
    """
    Finds all the winners in all tournaments for a given season.

    Parameters:
        season_code: Code of the season (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['tournaments']

    pipeline = [
        {'$match': {'season_code': season_code}},
        {
            '$lookup': {
                'from': 'teams',
                'localField': 'code',
                'foreignField': 'tournament_code',
                'as': 'teams'
            }
        },
        {'$unwind': '$teams'},
        {
            '$sort': {
                'teams.tournament_code': 1,
                'teams.overall_score': -1
            }
        },
        {
            '$group': {
                '_id': '$code',
                'tournament_name': {'$first': '$name'},
                'winner_team_name': {'$first': '$teams.name'},
                'winner_score': {'$first': '$teams.overall_score'}
            }
        },
        {
            '$project': {
                '_id': 0,
                'tournament_name': 1,
                'winner_team': 1,
                'winner_score': 1
            }
        }
    ]

    results = collection.aggregate(pipeline)

    for winner in results:
        print(winner)

    closeConnection(conn)
