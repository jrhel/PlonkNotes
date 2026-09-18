from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

import db_connection_handler

# The function queries the database for user information relating to the given username.
# If no user information is found pertainign to that username, the function returns True to indicate that the username is avalable.
# Else it returns False. 
def check_available_username(username: str):
    params = [username]
    result = db_connection_handler.query("SELECT * FROM User WHERE username = ?", params)
    if len(result) == 0:
        return True
    else:
        return False

def create_user(username: str, password: str):
    password_hash = generate_password_hash(password)
    params = [username, password_hash]
    db_connection_handler.execute("INSERT INTO User (username, password_hash) VALUES (?, ?)", params)
    # ! Needs to verify creation !