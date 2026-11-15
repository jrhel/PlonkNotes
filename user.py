from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

import db_connection_handler

# The function queries the database for user information relating to the given username.
# If no user information is found pertainign to that username, the function returns True to indicate that the username is avalable.
# Otherwise it returns False. 
def check_available_username(username: str):
    params = [username]
    result = db_connection_handler.query("SELECT * FROM User WHERE name = ?", params)
    if len(result) == 0:
        return True
    else:
        return False

def create_user(username: str, password: str):
    password_hash = generate_password_hash(password)
    db_connection_handler.execute("INSERT INTO User (name, password_hash) VALUES (?, ?)", [username, password_hash])
    # ! Needs to verify creation !

def verify_user(username: str, password: str):
    user_info = get_user(username)
    if user_info is None:
        return False
    return check_password_hash(user_info["password_hash"], password)

def get_user(username: str):
    params = [username]
    result = db_connection_handler.query("SELECT * FROM User WHERE name = ?", params)
    if len(result) == 0:
        return None
    else:
        return result[0]