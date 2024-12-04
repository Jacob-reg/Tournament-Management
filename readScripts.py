from utils import *


def view_universityProfile(university_code):
    """
    Finds and prints a university document based on its code.

    Parameter:
        university_code: Code of the university. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['universities']

    result = collection.find_one({"code": university_code})
    print(result)

    closeConnection(conn)


def view_playerProfile(player_code):
    """
    User views a player profile based on player code.

    Parameters:
        player_code: Code of the player. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['players']

    result = collection.find_one({"_code": player_code})
    print(result)

    closeConnection(conn)


def view_teamProfile(team_code):
    """
    User views a team profile based on team code.

    Parameter:
        team_code: Code of the team. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['teams']

    result = collection.find_one({"code": team_code})
    print(result)

    closeConnection(conn)


def view_teamMatches(tournament_code, team_code, status=None):
    """
    Finds matches of a team in a tournament, optionally filtering by status.

    Parameters:
        tournament_code: Code of the tournament. (String)
        team_code: Code of the team. (String)
        status: Status of the match (e.g., "Completed", "Ongoing"). (String, optional)
                If None, retrieves matches regardless of status.
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['matches']

    query = {
        "tournament_code": tournament_code,
        "$or": [
            {"team1.team_code": team_code},
            {"team2.team_code": team_code}
        ]
    }

    if status:
        query["status"] = status

    results = collection.find(query)

    for match in results:
        print(match)

    closeConnection(conn)


def view_tournamentMatches(tournament_code, status=None):
    """
    View matches in a tournament, optionally filtered by status.

    Parameters:
        tournament_code: Code of the tournament. (String)
        status: Status of the matches to filter by (e.g., "Completed", "Ongoing"). (String, optional).
                If None, retrieves all matches regardless of status.
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['matches']

    query = {"tournament_code": tournament_code}

    if status:
        query["status"] = status

    result = collection.find(query)

    for match in result:
        print(match)

    closeConnection(conn)


def view_leaderboard(tournament_code):
    """
    View a leaderboard of a tournament based on overall_score, sorted in descending order.

    Parameter:
        tournament_code: Code of the tournament. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['teams']

    # Aggregation pipeline to get leaderboard sorted by overall_score
    results = collection.aggregate([
        {
            "$match": {
                "tournament_code": tournament_code
            }
        },
        {
            "$project": {
                "name": 1,
                "overall_score": 1
            }
        },
        {
            "$sort": {
                "overall_score": -1
            }
        }
    ])

    for team in results:
        print(team)

    closeConnection(conn)


def view_topFour(tournament_code):
    """
    Finds and retrieves the top 4 teams of a tournament based on overall_score.

    Parameters:
        tournament_code: Code of the tournament. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['teams']

    results = collection.aggregate([
        {"$match": {"tournament_code": tournament_code}},
        {"$project": {"name": 1, "overall_score": 1}},
        {"$sort": {"overall_score": -1}},
        {"$limit": 4}
    ])

    # Print each team document as is
    for team in results:
        print(team)

    closeConnection(conn)


def view_winner(tournament_code):
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
        {"$match": {"tournament_code": tournament_code}},
        {"$project": {"name": 1, "overall_score": 1}},
        {"$sort": {"overall_score": -1}},
        {"$limit": 1}
    ])

    for winner in result:
        print(winner)

    closeConnection(conn)

def view_game_tournaments(game):
    """
    Finds a team and thier info
    
    Parameters:
        tournament_code: Code of the tournament. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['tournaments']
    
    result = collection.aggregate([
        {"$match": {"game": game}},
        {"$project": {"name": 1, "game": 1,"teams" : 1 "status" : 1}},
    ])

    for tournament in result:
        print(tournament)

    closeConnection(conn)

