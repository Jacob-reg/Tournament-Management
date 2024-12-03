def update_university(university_name, new_name, new_abbreviation):
    """
    Updates a  university document in the university collection.

    Parameters:
        university_name: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    Returns:
        inserted_id: ID of the created university document. (ObjectId)
    """

    conn = openConnection()
    db = conn['dbName']			        # Change dbName accordingly
    collection = db['universities']

    result = collection.update_one( 
{'name': university_name}, { 'name': new_name, 'abbreviation': new_abbreviation }} 
)
    print(f"{university_name}, ({abbreviation}) updated")

    closeConnection(conn)

    return result
