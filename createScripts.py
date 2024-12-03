from utils import *


def create_university(university_name, abbreviation):
    """
    Creates a new university document in the university collection.

    Parameters:
        university_name: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    Returns:
        inserted_id: ID of the created university document. (ObjectId)
    """

    conn = openConnection()
    db = conn['test']			        # Change dbName accordingly
    collection = db['universities']

    university = {
        'name': university_name,
        'abbreviation': abbreviation,
        'teams': []                     # Empty; no teams created yet.
    }

    result = collection.insert_one(university)
    print(f"{university_name} created with ID: {result.inserted_id}")

    closeConnection(conn)

    return result.inserted_id


def create_season(season_name, start_date, end_date, status):
    """
    Creates a new season document in the SEASONS collection.

    Parameters:
        name: Name of the UAAP Esports season (String)
        start_date: Start date of the season (datetime object)
        end_date: End date of the season (datetime object)
        status: Status of the season (String)

    Returns:
        inserted_id: ID of the created season document. (ObjectId)
    """

    conn = openConnection()
    db = conn['test']			        # Change dbName accordingly
    collection = db['seasons']

    season = {
        'name': season_name,
        'schedule': {
            'start_date': start_date,
            'end_date': end_date
        },
        'status': status,
        'tournaments': []               # Empty; no tournaments created yet.
    }

    result = collection.insert_one(season)
    print(f"{season_name} created with ID: {result.inserted_id}")

    closeConnection(conn)

    return result.inserted_id


def create_tournament(season_id, game, tournament_name, start_date, end_date, status):
    """
    Creates a new tournament document in the tournaments collection
    and adds the tournament to the season's tournaments array.

    Parameters:
        season_id: ID of the season (ObjectId).
        game: Name of the game (String).
        tournament_name: Name of the tournament (String).
        start_date: Tournament start date (ISODate).
        end_date: Tournament end date (ISODate).
        status: Status of the tournament (String).
    Returns:
        inserted_id: ID of the created tournament document. (ObjectId)
    """

    conn = openConnection()
    db = conn['test']			        # Change dbName accordingly
    tournaments_coll = db['tournaments']
    seasons_coll = db['seasons']

    # Insert the tournament into the tournaments collection
    tournament = {
        'season_id': season_id,
        'game': game,
        'name': tournament_name,
        'schedule': {
            'start_date': datetime(start_date),
            'end_date': datetime(end_date)
        },
        'status': status,
        'teams': [],                    # Empty; no teams created yet.
        'matches': []                   # Empty; no matches created yet.
    }

    result = tournaments_coll.insert_one(tournament)
    tournament_id = result.inserted_id

    print(f"{tournament_name} created with ID: {tournament_id}")

    # Add the tournament to the season's tournaments array
    seasons_coll.update_one(
        {'_id': season_id},
        {'$addToSet': {'tournaments': tournament_id}}
    )
    print(
        f"Tournament {tournament_name} added to the season with ID: {season_id}")

    closeConnection(conn)

    return result.inserted_id


def create_team(university_id, season_id, tournament_id, game, team_name, coach_fn, coach_ln):
    """
    Creates a new team document in the teams collection
    and adds new team to the university's teams array.

    Parameters:
        university_id: Reference to the university. (ObjectId)
        season_id: Reference to the season. (ObjectId)
        tournament_id: Reference to the tournament. (ObjectId)
        game: Game the team is associated with. (String)
        team_name: Name of the team. (String)
        coach_fn: Coach's first name. (String)
        coach_ln: Coach's last name. (String)

    Returns:
        inserted_id: ID of the created team document. (ObjectId)
    """

    conn = openConnection()
    db = conn['test']                # Change dbName accordingly
    teams_coll = db['teams']
    universities_coll = db['universities']

    # Insert the team into the teams collection
    team = {
        'university_id': university_id,
        'season_id': season_id,
        'tournament_id': tournament_id,
        'game': game,
        'name': team_name,
        'coach': {
            'first_name': coach_fn,
            'last_name': coach_ln
        },
        'roster': []
    }

    result = teams_coll.insert_one(team)
    team_id = result.inserted_id

    print(f"Team {team_name} created with ID: {team_id}")

    # Add the team to the university's teams array
    universities_coll.update_one(
        {'_id': university_id},
        {'$addToSet': {'teams': team_id}}
    )
    print(f"Team {team_name} added to the university with ID: {university_id}")

    closeConnection(conn)

    return team_id


def create_player(first_name, last_name, username, team_id):
    """
    Creates a new player document in the players collection 
    and add the player into their team's roster.

    Parameters:
        first_name: The player's first name. (String)
        last_name: The player's last name. (String)
        username: The player's in-game name. (String)
        team_id: The ID of the team the player is currently affiliated with. (ObjectId)

    Returns:
        inserted_id: ID of the created player document. (ObjectId)
    """

    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    players_coll = db['players']
    teams_coll = db['teams']

    # Insert the player into the players collection
    player = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "team_history": [
            {
                "team_id": team_id,
            }
        ]
    }

    result = players_coll.insert_one(player)
    player_id = result.inserted_id

    print(f"Player {first_name} {last_name} created with ID: {player_id}")

    # Add the player to the team's roster
    teams_coll.update_one(
        {"_id": team_id},
        {"$addToSet": {"roster": player_id}}
    )
    print(f"Player added to team roster for team ID: {team_id}")

    closeConnection(conn)

    return player_id


def create_match(tournament_id, start_date, end_date, match_type, status, team1, team2):
    """
    Creates a new match document in the matches collection 
    and adds the match to the tournament's matches array.

    Parameters:
        tournament_id: ID of the tournament (ObjectId).
        start_date: Match start date (ISODate).
        end_date: Match end date (ISODate).
        match_type: Type of the match (String).
        status: Status of the match (String).
        teams: List of dictionaries containing team details:
            [
                {
                    "team_id": ObjectId,
                    "lineup": [ObjectId],  # Array of player IDs
                    "score": Integer
                },
                ...
            ]
    """

    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    matches_coll = db['matches']
    tournaments_coll = db['tournaments']

    # Create the match document
    match = {
        'tournament_id': tournament_id,
        'schedule': {
            'start_date': datetime.fromisoformat(start_date),
            'end_date': datetime.fromisoformat(end_date)
        },
        'match_type': match_type,
        'status': status,
        'team1': {
            'team_id' : team1
            'score' : 0
        },
        'team2': {
            'team_id' : team2
            'score' : 0
        }
    }

    # Insert the match into the matches collection
    result = matches_coll.insert_one(match)
    match_id = result.inserted_id

    print(f"Match created with ID: {match_id}")

    # Add the match ID to the tournament's matches array
    tournaments_coll.update_one(
        {'_id': tournament_id},
        {'$addToSet': {'matches': match_id}}
    )
    print(
        f"Match {match_id} added to the tournament with ID: {tournament_id}")

    # Close the database connection
    closeConnection(conn)
