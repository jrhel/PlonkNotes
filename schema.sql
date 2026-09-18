CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);