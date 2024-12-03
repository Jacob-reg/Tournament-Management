def create_university(university_name, abbreviation):
    """
    Creates a new university document in the university collection.

    Parameters:
        university_name: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    Returns:
        inserted_id: ID of the created university document. (ObjectId)
    """

    conn = openConnection()
    db = conn['dbName']			        # Change dbName accordingly
    collection = db['universities']

    university = {
        'name': university_name,
        'abbreviation': abbreviation,
        'teams': []                     # Empty; no teams created yet.
    }

    result = collection.insert_one(university)
    print(f"{university_name} created with ID: {result.inserted_id}")

    closeConnection(conn)

    return result.inserted_id
