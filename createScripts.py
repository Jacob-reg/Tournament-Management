from utils import *


# Key generators (add explanation)
def generate_seasonCode(season_name):
    """
    Generates a custom season code based on the season name.

    Parameters:
        season_name: Name of the season (String).

    Returns:
        season_code: Custom code for the season (String).
    """

    # Assume the last word in the season name contains the season number
    return f"S{season_name.split()[-1]}"


def generate_tournamentCode(season_code, game):
    """
    Generates a custom tournament code based on the season code 
    and game abbreviation.

    Parameters:
        season_code: code of the season (String, e.g., "S86").
        game: Name of the game (String, e.g., "Mobile Legends Bang Bang").

    Returns:
        tournament_code: Custom code for the tournament (String, e.g., "S86-ML").
    """

    # Define a mapping of game names to abbreviations
    game_abbreviations = {
        "Valorant": "VALO",
        "Mobile Legends Bang Bang": "MLBB",
        "NBA 2K": "NBA",
    }

    # Use the mapping to get the abbreviation
    game_identifier = game_abbreviations.get(game)

    return f"{season_code}-{game_identifier}"


def generate_teamCode(team_name, university_code, tournament_code):
    """
    Generates a custom team code based on the team name and tournament code.

    Parameters:
        team_name: Name of the team (String).
        university_code: code of the university (String).
        tournament_code: code of the tournament (String).

    Returns:
        team_code: Custom code for the team (String).
    """

    # Generate abbreviation of the team name
    team_abbreviation = ''.join(word[0].upper() for word in team_name.split())

    # Combine team abbreviation with tournament code
    return f"{team_abbreviation}-{university_code}-{tournament_code}"


def generate_playerCode(first_name, last_name, username):
    """
    Generates a custom player code based on their full name
    and username.

    Parameters:
        first_name: The player's first name. (String)
        last_name: The player's last name. (String)
        username: The player's in-game name. (String)

    Returns:
        season_code: Custom code for the season (String).
    """

    clean_firstName = first_name.replace(" ", "")
    clean_lastName = last_name.replace(" ", "")

    return f"{clean_firstName}-{clean_lastName}-{username}"


def generate_matchCode(tournament_code, match_type, team1, team2):
    """
    Generates a custom key for a match document.

    Parameters:
        tournament_code: code of the tournament (String or String).
        match_type: Type of the match (String).
        team1: code of the first team (String).
        team2: code of the first team (String).

    Returns:
        match_code: Custom code for the match (String).
    """

    # Define match type abbreviations
    match_type_mapping = {
        'Round Robin': 'RR',
        'Semifinals': 'SF',
        'Finals': 'F'
    }

    # Get the abbreviation for the match type
    abbreviation = match_type_mapping.get(match_type, ''.join(
        [word[0].upper() for word in match_type.split()]))

    # Extract the first block of the team1 and team2 code
    team1_prefix = team1.split('-')[0]
    team2_prefix = team2.split('-')[0]

    return f"{tournament_code}-{abbreviation}-{team1_prefix}-{team2_prefix}"


def create_university(university_name, abbreviation):
    """
    Creates a new university document in the university collection.

    Parameters:
        university_name: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['universities']

    university = {
        'code': abbreviation,
        'name': university_name,
        'abbreviation': abbreviation,
        'teams': []                     # Empty; no teams created yet.
    }

    result = collection.insert_one(university)
    print(f"{university_name} created with ID and code: {result.inserted_id}, {abbreviation}")

    closeConnection(conn)


def create_season(season_name, start_date, end_date, status):
    """
    Creates a new season document in the SEASONS collection.

    Parameters:
        name: Name of the UAAP Esports season (String)
        start_date: Start date of the season (datetime object)
        end_date: End date of the season (datetime object)
        status: Status of the season (String)
    """

    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['seasons']

    season_code = generate_seasonCode(season_name)

    season = {
        'code': season_code,
        'name': season_name,
        'schedule': {
            'start_date': start_date,
            'end_date': end_date
        },
        'status': status,
        'tournaments': []               # Empty; no tournaments created yet.
    }

    result = collection.insert_one(season)
    print(f"{season_name} created with ID and code: {result.inserted_id}, {season_code}")

    closeConnection(conn)


def create_tournament(season_code, game, tournament_name, start_date, end_date, status):
    """
    Creates a new tournament document in the tournaments collection
    and adds the tournament to the season's tournaments array.

    Parameters:
        season_code: code of the season (String).
        game: Name of the game (String).
        tournament_name: Name of the tournament (String).
        start_date: Tournament start date (ISODate).
        end_date: Tournament end date (ISODate).
        status: Status of the tournament (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    tournaments_coll = db['tournaments']
    seasons_coll = db['seasons']

    tournament_code = generate_tournamentCode(season_code, game)

    # Insert the tournament into the tournaments collection
    tournament = {
        'code': tournament_code,
        'season_code': season_code,
        'game': game,
        'name': tournament_name,
        'schedule': {
            'start_date': start_date,
            'end_date': end_date
        },
        'status': status,
        'teams': [],                    # Empty; no teams created yet.
        'matches': []                   # Empty; no matches created yet.
    }

    result = tournaments_coll.insert_one(tournament)
    tournament_id = result.inserted_id

    print(f"{tournament_name} created with ID and code: {tournament_id}, {tournament_code}")

    # Add the tournament to the season's tournaments array
    seasons_coll.update_one(
        {'code': season_code},
        {'$addToSet': {'tournaments': tournament_code}}
    )
    print(
        f"Tournament {tournament_name} added to the season with code: {season_code}")

    closeConnection(conn)


def create_team(university_code, season_code, tournament_code, game, team_name, coach_fn, coach_ln):
    """
    Creates a new team document in the teams collection
    and adds new team to the university's teams array.

    Parameters:
        university_code: Reference to the university. (String)
        season_code: Reference to the season. (String)
        tournament_code: Reference to the tournament. (String)
        game: Game the team is associated with. (String)
        team_name: Name of the team. (String)
        coach_fn: Coach's first name. (String)
        coach_ln: Coach's last name. (String)
    """

    conn = openConnection()
    db = conn['uaap_esports']                # Change dbName accordingly
    teams_coll = db['teams']
    universities_coll = db['universities']
    tournaments_coll = db['tournaments']

    team_code = generate_teamCode(team_name, university_code, tournament_code)

    # Insert the team into the teams collection
    team = {
        'code': team_code,
        'university_code': university_code,
        'season_code': season_code,
        'tournament_code': tournament_code,
        'game': game,
        'name': team_name,
        'coach': {
            'first_name': coach_fn,
            'last_name': coach_ln
        },
        'roster': [],
        'overall_score': 0
    }

    result = teams_coll.insert_one(team)
    team_id = result.inserted_id

    print(f"Team {team_name} created with ID and code: {team_id}, {team_code}")

    # Add the team to the university's teams array
    universities_coll.update_one(
        {'code': university_code},
        {'$addToSet': {'teams': team_code}}
    )
    print(
        f"Team {team_name} added to the university with code: {university_code}")

    # Add the team to the university's teams array
    tournaments_coll.update_one(
        {'code': tournament_code},
        {'$addToSet': {'teams': team_code}}
    )
    print(
        f"Team {team_name} added to the tournament with code: {tournament_code}")

    closeConnection(conn)


def create_player(first_name, last_name, username, team_code):
    """
    Creates a new player document in the players collection 
    and add the player into their team's roster.

    Parameters:
        first_name: The player's first name. (String)
        last_name: The player's last name. (String)
        username: The player's in-game name. (String)
        team_code: The code of the team the player is currently affiliated with. (String)
    """

    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    players_coll = db['players']
    teams_coll = db['teams']

    player_code = generate_playerCode(first_name, last_name, username)

    # Insert the player into the players collection
    player = {
        'code': player_code,
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'team_history': [
            {
                'team_code': team_code,
            }
        ]
    }

    result = players_coll.insert_one(player)
    player_id = result.inserted_code

    print(
        f"Player {first_name} {last_name} created with ID and code: {player_id}, {player_code}")

    # Add the player to the team's roster
    teams_coll.update_one(
        {'code': team_code},
        {'$addToSet': {'code': player_code}}
    )
    print(
        f"Player {first_name} {last_name} is added to team roster for team code: {team_code}")

    closeConnection(conn)


def create_match(tournament_code, start_date, end_date, match_type, status, team1, team2):
    """
    Creates a new match document in the matches collection 
    and adds the match to the tournament's matches array.

    Parameters:
        tournament_code: code of the tournament (String).
        start_date: Match start date (ISODate).
        end_date: Match end date (ISODate).
        match_type: Type of the match (String).
        status: Status of the match (String).
        team1: code of the first team (String).
        team2: code of the second team (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    matches_coll = db['matches']
    tournaments_coll = db['tournaments']

    match_code = generate_matchCode(tournament_code, match_type, team1, team2)

    # Create the match document
    match = {
        'code': match_code,
        'tournament_code': tournament_code,
        'schedule': {
            'start_date': start_date,
            'end_date': end_date
        },
        'match_type': match_type,
        'status': status,
        'team1': {
            'team_code': team1,
            'score': 0
        },
        'team2': {
            'team_code': team2,
            'score': 0
        }
    }

    # Insert the match into the matches collection
    result = matches_coll.insert_one(match)
    match_id = result.inserted_id

    print(f"Match created with ID and code: {match_id}, {match_code}")

    # Add the match code to the tournament's matches array
    tournaments_coll.update_one(
        {'code': tournament_code},
        {'$addToSet': {'matches': match_code}}
    )
    print(
        f"Match {match_code} added to the tournament with code: {tournament_code}")

    # Close the database connection
    closeConnection(conn)
