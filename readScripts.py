def find_university():
    """
    Updates a  university document in the university collection.

    Parameters:
        university: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['test_tournament_management']			        # Change dbName accordingly
    collection = db['universities']

    result = collection.find()

    for doc in result:
      print(doc)

    closeConnection(conn)
