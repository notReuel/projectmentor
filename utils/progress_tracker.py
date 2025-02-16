import json
import os

def save_progress(results, filename="progress_data.json"):
    """Save assessment results to a JSON file."""
    data = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append(results)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Progress saved to {filename}")

def load_progress(filename="progress_data.json"):
    """Load assessment results from a JSON file."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def display_progress(results):
    """Display a summary of the assessment results."""
    print("\n=== Assessment Summary ===")
    print("Reading Level:", results.get("reading_level", "N/A"))
    print("Math Level:", results.get("math_level", "N/A"))
    print("Writing Assessment Completed:", results.get("writing_assessment_completed", False))
    print("==========================\n")
