# utils/lesson_planner.py

def generate_lesson_plan(results):
    """
    Generate a personalized lesson plan based on assessment results.
    'results' should be a dictionary containing:
      - reading_level (int): 1 (beginner) to 3 (advanced)
      - math_level (int): 1 (beginner) to 3 (advanced)
      - writing_assessment_completed (bool)
    
    Returns a lesson plan dictionary with recommended hours for each subject.
    """
    # Base allocation (in hours) for a 100-hour curriculum
    base_reading = 40
    base_writing = 30
    base_math = 30

    # Adjust Reading Hours: If not advanced, add extra reading practice
    reading_level = results.get("reading_level", 1)
    if reading_level < 3:
        base_reading += (3 - reading_level) * 5  # e.g., beginner gets +10 hours

    # Adjust Math Hours: If not advanced, add extra math practice
    math_level = results.get("math_level", 1)
    if math_level < 3:
        base_math += (3 - math_level) * 5  # e.g., beginner gets +10 hours

    # Adjust Writing Hours: If writing wasn't fully mastered, add extra practice
    writing_completed = results.get("writing_assessment_completed", False)
    if not writing_completed:
        base_writing += 10

    total_hours = base_reading + base_writing + base_math

    lesson_plan = {
        "total_hours": total_hours,
        "reading_hours": base_reading,
        "writing_hours": base_writing,
        "math_hours": base_math,
    }
    return lesson_plan

def display_lesson_plan(plan):
    """Display the generated lesson plan."""
    print("\n=== Personalized Lesson Plan ===")
    print(f"Total Hours: {plan['total_hours']}")
    print(f"Reading: {plan['reading_hours']} hours")
    print(f"Writing: {plan['writing_hours']} hours")
    print(f"Math: {plan['math_hours']} hours")
    print("===============================")

if __name__ == "__main__":
    # For testing purposes with sample results
    sample_results = {
        "reading_level": 1,
        "math_level": 2,
        "writing_assessment_completed": True
    }
    plan = generate_lesson_plan(sample_results)
    display_lesson_plan(plan)
