from utils import *


def add_teamPlayer(team_code, player_code):
    """
    Adds a player to a team's roster and updates the player's team history.

    Parameters:
        team_code: The code of the team to update. (String)
        player_code: The code of the player to add. (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    teams_coll = db['teams']
    players_coll = db['players']

    teams_coll.update_one(
        {'code': team_code},
        {'$addToSet': {'roster': player_code}}
    )

    players_coll.update_one(
        {'code': player_code},
        {'$addToSet': {'team_history': {'team_code': team_code}}}
    )

    closeConnection(conn)


def update_scores(match_code, team1_score, team2_score):
    """
    Increments the scores of the teams in a match and adds the same increments 
    to the overall_score field of each team.

    Parameters:
        match_code: The code of the match to update. (String)
        team1_score: The score increment for team 1. (Integer)
        team2_score: The score increment for team 2. (Integer)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    matches_coll = db['matches']
    teams_coll = db['teams']

    # Fetch the match document
    match = matches_coll.find_one({'code': match_code})
    team1_code = match['team1']['team_code']
    team2_code = match['team2']['team_code']

    # Increment the scores in the match document
    matches_coll.update_one(
        {'code': match_code},
        {
            '$inc': {
                'team1.score': team1_score,
                'team2.score': team2_score
            }
        }
    )

    teams_coll.update_one(
        {'code': team1_code},
        {'$inc': {'overall_score': team1_score}}
    )

    teams_coll.update_one(
        {'code': team2_code},
        {'$inc': {'overall_score': team2_score}}
    )

    closeConnection(conn)


def update_seasonStatus(season_code, new_status):
    """
    Updates the status of a season in the database.

    Parameters:
        season_code: Code of the season to update. (String)
        new_status: The new status to set (e.g., "Ongoing", "Completed"). (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['seasons']

    result = collection.update_one(
        {"code": season_code},
        {"$set": {"status": new_status}}
    )

    # Print the result
    if result.matched_count > 0:
        print(f"Season {season_code} status updated to '{new_status}'.")
    else:
        print(f"No season found with code {season_code}.")

    closeConnection(conn)


def update_tournamentStatus(tournament_code, new_status):
    """
    Updates the status of a tournament in the database.

    Parameters:
        tournament_code: Code of the tournament to update. (String)
        new_status: The new status to set (e.g., "Ongoing", "Completed"). (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['tournaments']

    result = collection.update_one(
        {"code": tournament_code},
        {"$set": {"status": new_status}}
    )

    if result.matched_count > 0:
        print(
            f"Tournament '{tournament_code}' status successfully updated to '{new_status}'.")
    else:
        print(f"No tournament found with code '{tournament_code}'.")

    closeConnection(conn)


def update_matchStatus(match_code, new_status):
    """
    Updates the status of a match in the database.

    Parameters:
        match_code: Code of the match to update. (String)
        new_status: The new status to set (e.g., "Scheduled", "Ongoing", "Completed"). (String)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    collection = db['matches']

    result = collection.update_one(
        {"code": match_code},
        {"$set": {"status": new_status}}
    )

    if result.matched_count > 0:
        print(
            f"Match '{match_code}' status successfully updated to '{new_status}'.")
    else:
        print(f"No match found with code '{match_code}'.")

    closeConnection(conn)


def update_season_schedule(season_code, new_start_date, new_end_date):
    """
    Updates the schedule of a season.

    Parameters:
        season_code: The code of the season to update. (String)
        new_start_date: The new start date of the season. (datetime or ISODate)
        new_end_date: The new end date of the season. (datetime or ISODate)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    seasons_coll = db['seasons']

    # Update the season schedule
    seasons_coll.update_one(
        {'code': season_code},
        {
            '$set': {
                'schedule.start_date': new_start_date,
                'schedule.end_date': new_end_date
            }
        }
    )

    closeConnection(conn)


def update_tournamentSchedule(tournament_code, new_start_date, new_end_date):
    """
    Updates the schedule of a tournament.

    Parameters:
        tournament_code: The code of the tournament to update. (String)
        new_start_date: The new start date of the tournament. (datetime or ISODate)
        new_end_date: The new end date of the tournament. (datetime or ISODate)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    tournaments_coll = db['tournaments']

    # Update the tournament schedule
    tournaments_coll.update_one(
        {'code': tournament_code},
        {
            '$set': {
                'schedule.start_date': new_start_date,
                'schedule.end_date': new_end_date
            }
        }
    )

    closeConnection(conn)


def update_matchSchedule(match_code, new_start_date, new_end_date):
    """
    Updates the schedule of a match.

    Parameters:
        match_code: The code of the match to update. (String)
        new_start_date: The new start date of the match. (datetime or ISODate)
        new_end_date: The new end date of the match. (datetime or ISODate)
    """
    conn = openConnection()
    db = conn['uaap_esports']  # Change dbName accordingly
    matches_coll = db['matches']

    # Update the schedule
    matches_coll.update_one(
        {'code': match_code},
        {
            '$set': {
                'schedule.start_date': new_start_date,
                'schedule.end_date': new_end_date
            }
        }
    )

    closeConnection(conn)
