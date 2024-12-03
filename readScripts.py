def find_university():
    """
    Updates a  university document in the university collection.

    Parameters:
        university: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['dbName']			        # Change dbName accordingly
    collection = db['universities']

    result = collection.find()

    for doc in result:
      print(doc)
    print(f"{university}, ({abbreviation}) updated")

    closeConnection(conn)

    return result
