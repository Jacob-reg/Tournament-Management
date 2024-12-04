from utils import *

def find_university():
    """
    Updates a  university document in the university collection.

    Parameters:
        university: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['universities']

    result = collection.find()

    for doc in result:
      print(doc)

    closeConnection(conn)

def viewPlayerProfile(playerID):
    """
    Access Pattern:
    View Player Profile: User views player profile
    """

    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['players']

    result = collection.find_one({"_id": playerID})
    
    for doc in result:
      print(doc)

    closeConnection(conn)

def viewTeamProfile(playerID):
    """
    Access Pattern:
    View Team Profile: User views team profile
    """

    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['players']

    result = collection.find_one({"_id": teamID})
    
    for doc in result:
      print(doc)

    closeConnection(conn)




def teamTournamentHistory(teamID):
    """
    Access Pattern:
    View Team Tournament Hisoty: User team tournament history
    """
    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['tournament']


    collection.aggregate[
        {(
            $match: {
                teams: { $in: [teamID] }
            }
        },
        {
            $project: {
                _id: 1
            }
        }
    ])
    closeConnection(conn)


def viewLeaderboard(tournament_id);

    """
    Access Pattern:
    View  a leaderboard of a tournament
    """
    conn = openConnection()
    db = conn['uaap_esports']			        # Change dbName accordingly
    collection = db['teams']

    collection.aggregate([
        {
            $match: {
                "tournament_id": tournament_id 
            }
        },
        {
            $project: {
                "name": 1,
                "wins": 1
                 }
        }, 
                {
            $sort: { 
                wins: -1 
                } 
        }, 
    ])
    closeConnection(conn)


