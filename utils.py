from pymongo import MongoClient
from datetime import *


def openConnection():
    conn_str = "mongodb+srv://group2:X4uXl32bccZhFPTr@g2-csci112finalproj.cdyb2.mongodb.net/?retryWrites=true&w=majority&appName=G2-CSCI112FinalProj"
    conn = MongoClient(conn_str)
    return conn


def closeConnection(conn):
    conn.close()