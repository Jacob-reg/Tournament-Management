from utils import *


def delete_university(university_id):
    """
    Deletes a university document from the universities collection.

    Parameters:
        university_id: The ID of the university to delete (String).
    """
    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    universities_coll = db['universities']

    result = universities_coll.delete_one({'_id': university_id})
    if result.deleted_count > 0:
        print(f"University with ID {university_id} deleted successfully.")
    else:
        print(f"University with ID {university_id} not found.")

    closeConnection(conn)


def delete_season(season_id):
    """
    Deletes a season document from the seasons collection.

    Parameters:
        season_id: The ID of the season to delete (String).
    """
    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    seasons_coll = db['seasons']

    result = seasons_coll.delete_one({'_id': season_id})
    if result.deleted_count > 0:
        print(f"Season with ID {season_id} deleted successfully.")
    else:
        print(f"Season with ID {season_id} not found.")

    closeConnection(conn)


def delete_tournament(tournament_id):
    """
    Deletes a tournament document from the tournaments collection.

    Parameters:
        tournament_id: The ID of the tournament to delete (String).
    """
    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    tournaments_coll = db['tournaments']

    result = tournaments_coll.delete_one({'_id': tournament_id})
    if result.deleted_count > 0:
        print(f"Tournament with ID {tournament_id} deleted successfully.")
    else:
        print(f"Tournament with ID {tournament_id} not found.")

    closeConnection(conn)


def delete_team(team_id):
    """
    Deletes a team document from the teams collection.

    Parameters:
        team_id: The ID of the team to delete (String).
    """
    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    teams_coll = db['teams']

    result = teams_coll.delete_one({'_id': team_id})
    if result.deleted_count > 0:
        print(f"Team with ID {team_id} deleted successfully.")
    else:
        print(f"Team with ID {team_id} not found.")

    closeConnection(conn)


def delete_player(player_id):
    """
    Deletes a player document from the players collection.

    Parameters:
        player_id: The ID of the player to delete (String).
    """
    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    players_coll = db['players']

    result = players_coll.delete_one({'_id': player_id})
    if result.deleted_count > 0:
        print(f"Player with ID {player_id} deleted successfully.")
    else:
        print(f"Player with ID {player_id} not found.")

    closeConnection(conn)


def delete_match(match_id):
    """
    Deletes a match document from the matches collection.

    Parameters:
        match_id: The ID of the match to delete (String).
    """
    conn = openConnection()
    db = conn['test']  # Change dbName accordingly
    matches_coll = db['matches']

    result = matches_coll.delete_one({'_id': match_id})
    if result.deleted_count > 0:
        print(f"Match with ID {match_id} deleted successfully.")
    else:
        print(f"Match with ID {match_id} not found.")

    closeConnection(conn)
