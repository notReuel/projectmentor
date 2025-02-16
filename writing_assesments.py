import random

def generate_writing_prompt(level):
    """Generate a writing prompt based on difficulty level."""
    basic_prompts = [
        "Write the alphabet from A to Z.",
        "Copy this sentence: The cat is on the mat.",
        "Write your name three times."
    ]
    
    sentence_prompts = [
        "Complete this sentence: The dog ran _____.",
        "Arrange these words into a sentence: school - to - go - I - love",
        "Write a sentence using the word 'happy'."
    ]
    
    creative_prompts = [
        "Write a short story about a lost balloon.",
        "Describe your favorite food in five sentences.",
        "Write a letter to a friend about your day."
    ]
    
    if level == 1:
        return random.choice(basic_prompts)
    elif level == 2:
        return random.choice(sentence_prompts)
    else:
        return random.choice(creative_prompts)

def assess_writing():
    """Guide the child through a writing assessment."""
    print("Let's test your writing skills!")
    level = 1
    while level <= 3:
        prompt = generate_writing_prompt(level)
        print(f"Your writing task: {prompt}")
        input("Press Enter when you have completed the task.")
        print("Great job! Let's move to the next task.")
        level += 1
    
    print("Writing assessment complete!")

if __name__ == "__main__":
    assess_writing()
