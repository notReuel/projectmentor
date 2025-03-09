"""
progress_tracker.py

Functions to save and load learner progress to/from a JSON file.
"""

import json
import os

def save_progress(progress, filename="progress_data.json"):
    """
    Save progress data to a JSON file.
    
    Args:
        progress (dict): Progress data to save.
        filename (str): The filename to save the data in.
    """
    data = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append(progress)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Progress saved to {filename}")

def load_progress(filename="progress_data.json"):
    """
    Load progress data from a JSON file.
    
    Args:
        filename (str): The filename to load data from.
        
    Returns:
        list: A list of progress data dictionaries.
    """
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def display_progress(progress):
    """
    Display progress data (for debugging/CLI purposes).
    
    Args:
        progress (dict): A dictionary containing progress data.
    """
    print("\n=== Progress Data ===")
    for key, value in progress.items():
        print(f"{key}: {value}")
    print("=====================\n")

if __name__ == "__main__":
    # For testing purposes:
    dummy_progress = {
        "reading_level": 2,
        "math_level": 3,
        "writing_assessment_completed": True
    }
    save_progress(dummy_progress)
    loaded = load_progress()
    print("Loaded Progress:", loaded)
    display_progress(dummy_progress)
