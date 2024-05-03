import json

def load_user_data():
    """Load user data from a JSON file if it exists, otherwise return an empty dictionary."""
    try:
        with open("user_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(user_data):
    """Save user data to a JSON file."""
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)

def authenticate(username, password):
    """
    Authenticate a user with the provided username and password.
    
    Parameters:
        username (str): The username to authenticate.
        password (str): The password to check against the stored data.
    
    Returns:
        bool: True if the authentication is successful, False otherwise.
    """
    user_data = load_user_data()
    if username in user_data and user_data[username] == password:
        return True
    else:
        return False

def create_account(username, password):
    """
    Create a new account with the provided username and password.
    
    Parameters:
        username (str): The username for the new account.
        password (str): The password for the new account.
    
    Returns:
        bool: True if the account is successfully created, False if the username already exists.
    """
    user_data = load_user_data()
    if username in user_data:
        return False  # User already exists
    else:
        user_data[username] = password
        save_user_data(user_data)
        return True  # Account created successfully

