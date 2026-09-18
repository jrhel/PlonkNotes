import sqlite3

# Verifies integrity of database
def verify_database():
    user_table = "CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)"
    database = get_connection()
    database.execute(user_table)
    database.commit()
    database.close()

def get_connection():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection

def execute(statement: str, params=[]):
    connection = get_connection()
    result = connection.execute(statement, params).lastrowid
    connection.commit()
    connection.close()
    return result

def query(statement: str, params: [str]):
    connection = get_connection()
    result = connection.execute(statement, params).fetchall()
    connection.close()
    return result