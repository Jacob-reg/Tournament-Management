from utils import *


def update_university(university, new_name, new_abbreviation):
    """
    Updates a  university document in the university collection.

    Parameters:
        university: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['universities']

    result = collection.update_one(
        {'university': university},
        {'$set': {'university': new_name, 'abbreviation': new_abbreviation}}
    )

    closeConnection(conn)

    return result


def update_team(tournament_id, team_name, university_id, season_id, game, coach_fn, coach_ln):
    """
    Updates a  university document in the university collection.

    Parameters:
        university: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['universities']

    results = collection.update_one(
        {'tournament_id': tournament_id},
        {'$set': {'team_name': team_name, 'university_id': university_id,
                  'season_id': season_id, 'game': game, 'coach_fn': coach_fn, 'coach_ln': coach_ln}}
    )

    print(f"{team_name} updated")

    closeConnection(conn)

    return result


def updateMatchScore(match_id,team1_score, team2_score):
    """
    Update Score Access Pattern
    """
    conn = openConnection()
    db= conn['uaap_esports']
    collection = db['matches']

    results = collection.update_one(
        {"_id": 'S0-NBA-Elimination-M0'},
        {"$set": {"team1.0.score": team1_score}}
    )
    
    results = collection.update_one(
        {"_id": 'S0-NBA-Elimination-M0'},
        {"$set": {"team2.0.score": team2_score}}
    )

    closeConnection(conn)

def matchComplete(match_id):

    """
    Update Leaderboard Access Pattern
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['matches']

    results = collection.update_one(
        {"_id": 'S0-NBA-Elimination-M0'},
        {"$set": {"Status": "Complete"}}
    )

    

    closeConnection(conn)
