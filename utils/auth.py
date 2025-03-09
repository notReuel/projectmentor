# utils/auth.py
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()

class User(UserMixin):
    """
    Simple User class for demonstration purposes.
    In production, integrate this with your Learner model in the database.
    """
    def __init__(self, id, email, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash

# Dummy in-memory user store
dummy_users = {}

def register_user(email, password):
    """
    Register a new user.
    
    Args:
        email (str): User's email address.
        password (str): Plain text password.
    
    Returns:
        User: The newly created User object.
    """
    # Check if the email already exists (dummy check)
    for user in dummy_users.values():
        if user.email == email:
            return None  # In production, handle duplicate registration appropriately.
    new_id = str(len(dummy_users) + 1)
    password_hash = generate_password_hash(password)
    user = User(new_id, email, password_hash)
    dummy_users[new_id] = user
    return user

def get_user(user_id):
    """
    Retrieve a user by their ID.
    
    Args:
        user_id (str): The unique user ID.
    
    Returns:
        User or None: The User object if found.
    """
    return dummy_users.get(user_id)

def verify_password(stored_hash, password):
    """
    Verify a password against its stored hash.
    
    Args:
        stored_hash (str): The hashed password.
        password (str): The plaintext password to check.
    
    Returns:
        bool: True if the password is correct.
    """
    return check_password_hash(stored_hash, password)

@login_manager.user_loader
def load_user(user_id):
    """
    Flask-Login user loader callback.
    """
    return get_user(user_id)

if __name__ == "__main__":
    # For testing: Register a user and try to retrieve it.
    test_user = register_user("test@example.com", "password")
    if test_user:
        print("Registered user:", test_user.email)
    else:
        print("User already exists.")
    print("Retrieved user:", get_user("1"))
