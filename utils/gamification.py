"""
gamification.py

Provides functions for awarding badges based on assessment results.
"""

def award_badges(results):
    """
    Award badges based on the assessment results.
    
    Args:
        results (dict): Assessment results containing keys like 'reading_level',
                        'math_level', and 'writing_assessment_completed'.
                        
    Returns:
        list: A list of badges awarded.
    """
    badges = []
    if results.get("reading_level", 0) >= 2:
        badges.append("Reading Prodigy")
    if results.get("math_level", 0) >= 2:
        badges.append("Math Whiz")
    if results.get("writing_assessment_completed", False):
        badges.append("Writing Star")
    return badges

def display_badges(badges):
    """
    Display awarded badges (for CLI or debugging purposes).
    
    Args:
        badges (list): List of badge names.
    """
    if badges:
        print("\nCongratulations! You've earned the following badges:")
        for badge in badges:
            print(f"- {badge}")
    else:
        print("\nKeep working hard to earn badges!")
