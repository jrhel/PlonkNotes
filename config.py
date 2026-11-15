import secrets

# Reads the secret session key from the locally stored file "kingdom.txt". If the file does not exist, generate_session_key() is called upon to generate it and return the session key. Finally, this function also returns the session key.
def get_session_key():
    session_key = ""
    try:
        with open("kingdom.txt") as kingdom:
            session_key = kingdom.read()
            
    except FileNotFoundError:
       session_key = generate_session_key()

    return session_key

# Generates a secret session key to be stored locally, creates the file "kingdom.txt", and stores the session key in it. Finally, get_session_key() is called upon to verify successul storage and return the key.
def generate_session_key():
    key = secrets.token_hex(32)
    with open("kingdom.txt", "w") as kingdom:
        kingdom.write(key)
    
    return get_session_key()