from pymongo import MongoClient
from datetime import *


def openConnection():
    conn_str = "mongodb+srv://group2:X4uXl32bccZhFPTr@g2-csci112finalproj.cdyb2.mongodb.net/?retryWrites=true&w=majority&appName=G2-CSCI112FinalProj"
    conn = MongoClient(conn_str)
    return conn


def closeConnection(conn):
    conn.close()


db_name = 'testOne'
collections = [
    'universities',
    'seasons',
    'tournaments',
    'teams',
    'players',
    'matches'
]


def setUniqueIndex():
    """
    Creates a unique index on the specified field 
    in the list of collections.
    """
    conn = openConnection()

    db = conn[db_name]
    for collection_name in collections:
        collection = db[collection_name]
        result = collection.create_index([('code', 1)], unique=True)
        print(
            f"Unique index created on 'code' in collection '{collection_name}': {result}")

    closeConnection(conn)
