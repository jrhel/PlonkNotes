import sqlite3

# Verifies integrity of database
def verify_database():
    schema = [
        "CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)",
        "CREATE TABLE IF NOT EXISTS Producer (id INTEGER PRIMARY KEY, name TEXT UNIQUE)",
        "CREATE TABLE IF NOT EXISTS Country (id INTEGER PRIMARY KEY, name TEXT UNIQUE)",
        "CREATE TABLE IF NOT EXISTS Region (id INTEGER PRIMARY KEY, region TEXT UNIQUE, parent_region_id INTEGER, country_id INTEGER, FOREIGN KEY (parent_region_id) REFERENCES Region(id), FOREIGN KEY (country_id) REFERENCES Country(id))",
        "CREATE TABLE IF NOT EXISTS Apellation (id INTEGER PRIMARY KEY, name TEXT UNIQUE)",
        "CREATE TABLE IF NOT EXISTS Variety (id INTEGER PRIMARY KEY, grape TEXT UNIQUE)",
        "CREATE TABLE IF NOT EXISTS Type (id INTEGER PRIMARY KEY, name TEXT UNIQUE)",
        "CREATE TABLE IF NOT EXISTS Wine (id INTEGER PRIMARY KEY, name TEXT, producer_id INTEGER, appellation_id INTEGER, country_id INTEGER, region_id INTEGER, FOREIGN KEY (producer_id) REFERENCES Producer(id), FOREIGN KEY (appellation_id) REFERENCES Appellation(id), FOREIGN KEY (country_id) REFERENCES Country(id), FOREIGN KEY (region_id) REFERENCES Region(id))",
        "CREATE TABLE IF NOT EXISTS Wine (wine_id INTEGER REFERENCES Wine(id), variety_id INTEGER REFERENCES Variety(id))",
        "CREATE TABLE IF NOT EXISTS WineType (wine_id INTEGER REFERENCES Wine(id), type_id INTEGER REFERENCES Type(id))"
    ]
    
    database = get_connection()
    for table in schema:
        database.execute(table)    
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