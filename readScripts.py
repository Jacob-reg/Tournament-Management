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
