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

    results = collection.update_one(
<< << << < HEAD
        {'university': university},
        {'$set': {'university': new_name, 'abbreviation': new_abbreviation}}
    )


== == == =
    {'university': university},
    {'$set': {'university': new_name, 'abbreviation': abbreviation}}
    )

>> >>>> > 94dce6c3408e9f1b5410b9ba65541bebf47dde05
    print(f"{university}, ({abbreviation}) updated")

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
    db= conn['uaap_esports']
    collection = db['universities']

    results = collection.update_one(
    {'tournament_id': tournament_id},
    {'$set': {'team_name': team_name, 'university_id': university_id,
        'season_id': season_id, 'game': game, 'coach_fn': coach_fn, 'coach_ln': coach_ln}}
    )

    print(f"{team_name} updated")

    closeConnection(conn)

    return result

def updateMatchScoreteam1(match_id):
    """
    Update Score Access Pattern
    """
    conn = openConnection()
    db= conn['uaap_esports']
    collection = db['matches']

    results = collection.update_one(
    {'match_id': match_id},
    {"$inc": {"team1.score": 1}}
    )

    closeConnection(conn)

def updateMatchScoreteam2(match_id):
    """
    Update Score Access Pattern
    """
    conn = openConnection()
    db= conn['uaap_esports']
    collection = db['matches']

    results = collection.update_one(
    {'match_id': match_id},
    {"$inc": {"team2.score": 1}}
    )

    closeConnection(conn)

def matchComplete(match_id):

    """
    Update Leaderboard Access Pattern
    """

    conn = openConnection()
    db = conn['uaap_esports']
    collection = db['matches']

    if
    collection.aggregate([
            {$match: {
                    team1.score: 2
                }
            },
            {$project: {
                    _id: 1
                }
            }
        ])

    closeConnection(conn)
