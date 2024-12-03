from utils import *


def update_university(university, new_name, new_abbreviation):
    """
    Updates a  university document in the university collection.

    Parameters:
        university: Name of the university. (String)
        abbreviation: Abbreviation of the university (String).
    """

    conn = openConnection()
    db = conn['dbName']			        # Change dbName accordingly
    collection = db['universities']

    results = collection.update_one(
        {'university': university},
        {'$set': {'university': new_name, 'abbreviation': new_abbreviation}}
    )

    print(f"{university}, ({abbreviation}) updated")

    closeConnection(conn)

    return result
