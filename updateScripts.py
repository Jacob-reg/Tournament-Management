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


def completeMatchScore(match_id, winner):
    """
    Complete match and update wins access pattern
    """
    conn = openConnection()
    db= conn['uaap_esports']
    teamcoll = db['teams']
    matchcoll = db['matches']
    
    results = teamcoll.update_one(
        {"_id": winner},
        { $inc: { wins: 1 }}
    )
    
    results = matchcoll.update_one(
        {"_id": match_id},
        {"$set": {"Status": "Complete"}}
    )


    closeConnection(conn)
