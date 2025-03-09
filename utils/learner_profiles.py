"""
learner_profiles.py

Manages learner profiles by saving and retrieving data from a JSON file.
"""

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
        learner_id (str): The unique identifier for the learner.
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
        learner_id (str): The unique identifier for the learner.
        
    Returns:
        dict or None: The learner profile if found, otherwise None.
    """
    profiles = load_profiles()
    return profiles.get(learner_id, None)

def generate_learner_profile(results):
    """
    Generate a learner profile summary based on assessment results.
    
    Args:
        results (dict): Dictionary containing keys 'reading_level', 'math_level',
                        and 'writing_assessment_completed'.
                        
    Returns:
        dict: A learner profile including a category and a message.
    """
    reading_level = results.get("reading_level", 1)
    math_level = results.get("math_level", 1)
    writing_completed = results.get("writing_assessment_completed", False)
    
    # Categorize learner based on performance
    if reading_level <= 1 and math_level <= 1:
        category = "Beginner"
        message = "You are starting your learning journey!"
    elif reading_level == 2 and math_level == 2:
        category = "Intermediate"
        message = "You're making good progress!"
    else:
        category = "Advanced"
        message = "You are doing great!"
    
    return {
        "category": category,
        "message": message,
        "writing_completed": writing_completed
    }

if __name__ == "__main__":
    # For testing purposes:
    test_id = "learner123"
    print("Learner profile for", test_id, ":", get_learner(test_id))
    # Example: generating a profile from dummy results
    dummy_results = {
        "reading_level": 2,
        "math_level": 2,
        "writing_assessment_completed": True
    }
    generated = generate_learner_profile(dummy_results)
    print("Generated Learner Profile:", generated)
