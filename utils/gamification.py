# utils/gamification.py

def award_badges(results):
    """
    Award badges based on the assessment results.
    Returns a list of badges earned.
    """
    badges = []
    
    # Award a badge for strong reading skills
    if results.get("reading_level", 0) >= 2:
        badges.append("Reading Prodigy")
    
    # Award a badge for strong math skills
    if results.get("math_level", 0) >= 2:
        badges.append("Math Whiz")
    
    # Award a badge for completing the writing assessment
    if results.get("writing_assessment_completed", False):
        badges.append("Writing Star")
    
    return badges

def display_badges(badges):
    """
    Display the awarded badges.
    """
    if badges:
        print("\nCongratulations! You've earned the following badges:")
        for badge in badges:
            print(f"- {badge}")
    else:
        print("\nKeep working hard to earn badges!")
