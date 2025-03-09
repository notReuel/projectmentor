"""
analytics.py

Provides functions to load progress data from a JSON file, aggregate analytics,
display analytics, and calculate progress improvements.
"""

import json
import os

def load_progress(filename="progress_data.json"):
    """Load assessment results from a JSON file."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def aggregate_results():
    """Aggregate progress data to compute average reading and math levels."""
    data = load_progress()
    if not data:
        print("No progress data available.")
        return {}
    
    total_reading = sum(item.get("reading_level", 0) for item in data)
    total_math = sum(item.get("math_level", 0) for item in data)
    count = len(data)
    
    aggregated = {
        "total_assessments": count,
        "avg_reading_level": total_reading / count,
        "avg_math_level": total_math / count
    }
    return aggregated

def display_aggregated_results(aggregated):
    """Display aggregated performance data."""
    print("\n=== Aggregated Performance Analytics ===")
    print(f"Total Assessments: {aggregated.get('total_assessments', 0)}")
    print(f"Average Reading Level: {aggregated.get('avg_reading_level', 0):.2f}")
    print(f"Average Math Level: {aggregated.get('avg_math_level', 0):.2f}")
    print("==========================================\n")

def calculate_progress(previous, current):
    """
    Calculate the percentage improvement in reading and math levels.

    Args:
        previous (dict): Dictionary containing previous scores.
        current (dict): Dictionary containing current scores.

    Returns:
        dict: Progress in percentage for each skill.
    """
    progress = {}
    for key in ["reading_level", "math_level"]:
        prev = previous.get(key, 0)
        curr = current.get(key, 0)
        if prev == 0:  # Avoid division by zero
            progress[f"{key}_improvement"] = 100 if curr > 0 else 0
        else:
            progress[f"{key}_improvement"] = ((curr - prev) / prev) * 100
    return progress

if __name__ == "__main__":
    agg = aggregate_results()
    if agg:
        display_aggregated_results(agg)