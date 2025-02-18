# utils/learner_profiles.py
import json
import os

PROFILE_FILENAME = "learner_profiles.json"

def load_profiles():
    """Load learner profiles from a JSON file."""
    if os.path.exists(PROFILE_FILENAME):
        with open(PROFILE_FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_profiles(profiles):
    """Save learner profiles to a JSON file."""
    with open(PROFILE_FILENAME, "w") as file:
        json.dump(profiles, file, indent=4)

def add_or_update_learner(learner_id, new_data):
    """
    Add a new learner or update an existing learner's profile.
    
    Args:
        learner_id (str): The unique ID of the learner.
        new_data (dict): A dictionary containing assessment results and additional data.
    """
    profiles = load_profiles()
    profiles[learner_id] = new_data
    save_profiles(profiles)
    print(f"Learner profile for '{learner_id}' has been updated.")

def get_learner(learner_id):
    """
    Retrieve a learner's profile by their ID.
    
    Args:
        learner_id (str): The unique ID of the learner.
    
    Returns:
        dict or None: The learner profile if found, otherwise None.
    """
    profiles = load_profiles()
    return profiles.get(learner_id, None)

if __name__ == "__main__":
    # For testing purposes
    test_id = "learner123"
    print("Learner profile for", test_id, ":", get_learner(test_id))
