# utils/auth.py
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()

class User(UserMixin):
    # In a production system, you would integrate this with your database (e.g., the Learner model)
    def __init__(self, id, email, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash

# Dummy user store for testing purposes.
# Replace this with a proper database query in production.
dummy_users = {
    "1": User("1", "test@example.com", generate_password_hash("password"))
}

def get_user(user_id):
    """
    Retrieve a user from the dummy user store.
    
    Args:
        user_id (str): The unique user ID.
        
    Returns:
        User: A User object if found, otherwise None.
    """
    return dummy_users.get(user_id)

def hash_password(password):
    """
    Hash a password for storing.
    
    Args:
        password (str): The plaintext password.
        
    Returns:
        str: The hashed password.
    """
    return generate_password_hash(password)

def verify_password(stored_hash, password):
    """
    Verify a stored password hash against a provided password.
    
    Args:
        stored_hash (str): The stored hashed password.
        password (str): The plaintext password to verify.
        
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return check_password_hash(stored_hash, password)
