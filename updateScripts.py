def update_university(university, new_name, abbreviation):
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
    {'$set': {'university': new_name, 'abbreviation': abbreviation}}
    )  
    
    print(f"{university}, ({abbreviation}) updated")

    closeConnection(conn)

    return result

def update_team(tournament_id, team_name, university_id, season_id, game, coach_fn, coach_ln ):
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
    {'tournament_id': tournament_id},
    {'$set': {'team_name': team_name, 'university_id': university_id, 'season_id': season_id
             , 'game': game, 'coach_fn': coach_fn, 'coach_ln': coach_ln}}
    )  
    
    print(f"{team_name} updated")

    closeConnection(conn)

    return result
