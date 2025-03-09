"""
lesson_planner.py

Generates a personalized lesson plan based on assessment results.
"""

def generate_lesson_plan(results):
    """
    Generate a personalized lesson plan based on assessment results.
    
    Args:
        results (dict): Dictionary containing keys 'reading_level', 'math_level',
                        and 'writing_assessment_completed'.
                        
    Returns:
        dict: A lesson plan with recommended hours for each subject.
    """
    # Base allocations (for a 100-hour curriculum)
    base_reading = 40
    base_writing = 30
    base_math = 30

    # Increase reading practice for lower levels
    reading_level = results.get("reading_level", 1)
    if reading_level < 3:
        base_reading += (3 - reading_level) * 5  # Additional hours for beginners

    # Increase math practice for lower levels
    math_level = results.get("math_level", 1)
    if math_level < 3:
        base_math += (3 - math_level) * 5

    # Increase writing hours if not completed
    writing_completed = results.get("writing_assessment_completed", False)
    if not writing_completed:
        base_writing += 10

    total_hours = base_reading + base_writing + base_math

    return {
        "total_hours": total_hours,
        "reading_hours": base_reading,
        "writing_hours": base_writing,
        "math_hours": base_math,
    }

def display_lesson_plan(plan):
    """
    Display the lesson plan (for CLI or debugging).
    
    Args:
        plan (dict): Lesson plan dictionary.
    """
    print("\n=== Personalized Lesson Plan ===")
    print(f"Total Hours: {plan['total_hours']}")
    print(f"Reading Hours: {plan['reading_hours']}")
    print(f"Writing Hours: {plan['writing_hours']}")
    print(f"Math Hours: {plan['math_hours']}")
    print("===================================")