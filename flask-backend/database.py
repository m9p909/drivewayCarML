import sqlite3

def setupDatabase():
    return sqlite3.connect('carml.db')