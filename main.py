import time
from assessments.adaptive_reading_assessment import get_reading_level, test_comprehension
from assessments.writing_assessment import assess_writing
from assessments.math_assessment import get_math_level
from utils.progress_tracker import save_progress, display_progress
from utils.gamification import award_badges, display_badges
from utils.lesson_planner import generate_lesson_plan  # We'll return the plan, not display it
from utils.learner_profiles import add_or_update_learner
from utils.analytics import aggregate_results

def start_assessment(learner_id):
    """
    Run all assessments for a given learner and return a dictionary of results.
    
    This function has been refactored to remove command-line inputs/outputs
    and is intended for use with Flask routes.
    """
    # Instead of printing and sleeping, we directly run the assessments.
    # Reading Assessment
    reading_level = get_reading_level()
    # Note: test_comprehension() may still produce dialogs if it uses Tkinter,
    # so you might need to adapt it further for web usage.
    test_comprehension()
    
    # Writing Assessment
    assess_writing()
    
    # Math Assessment
    math_level = get_math_level()
    
    # Compile results into a dictionary
    results = {
        "reading_level": reading_level,
        "math_level": math_level,
        "writing_assessment_completed": True
    }
    
    # Save progress and (if needed) display summary (for now, we'll save but not display via CLI)
    save_progress(results)
    # Optionally, you could call display_progress(results) in a terminal context,
    # but for web we want to return data.
    
    # Gamification: Award badges based on progress
    badges = award_badges(results)
    
    # Update learner profile
    add_or_update_learner(learner_id, results)
    
    # Generate a personalized lesson plan based on results
    lesson_plan = generate_lesson_plan(results)
    
    # Gather aggregated analytics data
    aggregated = aggregate_results()
    
    # Return all collected data so that Flask can render it in a template
    return {
        "results": results,
        "badges": badges,
        "lesson_plan": lesson_plan,
        "aggregated": aggregated
    }

# For debugging or command-line testing, you can include a main block:
if __name__ == '__main__':
    learner_id = input("Enter your learner ID (or email): ").strip()
    assessment_data = start_assessment(learner_id)
    print("Assessment Data:")
    print(assessment_data)
