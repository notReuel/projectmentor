import time
from assessments.adaptive_reading_test import get_reading_level, test_comprehension
from assessments.writing_assesment import assess_writing
from assessments.math_assessment import get_math_level
from utils.progress_tracker import save_progress, display_progress  # Assuming progress_tracker.py is in utils/
from utils.gamification import award_badges, display_badges
from utils.lesson_planner import generate_lesson_plan, display_lesson_plan
from utils.learner_profiles import add_or_update_learner, get_learner
from utils.analytics import aggregate_results, display_aggregated_results


def main():
    print("Welcome to the AI Tutor MVP!")
    print("=================================")
    time.sleep(1)

    # Get learner ID
    learner_id = input("Enter your learner ID (or email): ").strip()
    

    # Reading Assessments
    print("\nStarting Reading Assessment...")
    reading_level = get_reading_level()
    print(f"Your estimated reading level is: {reading_level}")
    test_comprehension()

    input("\nPress Enter to continue to the Writing Assessment...")
    
    # Writing Assessment
    print("\nStarting Writing Assessment...")
    assess_writing()
    
    input("\nPress Enter to continue to the Math Assessment...")
    
    # Math Assessment
    print("\nStarting Math Assessment...")
    math_level = get_math_level()
    print(f"Your estimated math level is: {math_level}")
    
    print("\nAll assessments complete!")
    print("Thank you for using the AI Tutor MVP!")
    
        # Compile results into a dictionary
    results = {
        "reading_level": reading_level,
        "math_level": math_level,
        "writing_assessment_completed": True
    }
    
    # Save progress and display summary
    save_progress(results)
    display_progress(results)
    
    # Gamification: Award and display badges based on progress
    badges = award_badges(results)
    display_badges(badges)
    
    # Update learner profile
    add_or_update_learner(learner_id, results)
    
    # Generate and display a personalized lesson plan based on results
    plan = generate_lesson_plan(results)
    display_lesson_plan(plan)

    # Ask if user wants to see aggregated analytics across all assessments
    if input("Would you like to view aggregated performance analytics? (y/n): ").strip().lower() == 'y':
        aggregated = aggregate_results()
        display_aggregated_results(aggregated)

if __name__ == '__main__':
    main()
