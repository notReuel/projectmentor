import random
from difflib import SequenceMatcher

def similarity_score(expected, actual):
    """Returns a similarity ratio between expected and actual text."""
    return SequenceMatcher(None, expected.lower(), actual.lower()).ratio()

def basic_writing_test():
    """Basic writing tasks: letter formation and spelling. Some tasks are auto-evaluated."""
    print("=== Basic Writing Test ===")
    # Each prompt is a tuple: (instruction, expected_answer)
    # If expected_answer is None, the task is open-ended.
    prompts = [
        ("Write the alphabet from A to Z.", None),
        ("Copy this sentence: The cat is on the mat.", "The cat is on the mat."),
        ("Write your name three times.", None),
        ("Write the numbers 1 to 20 in words.", None),
        ("Copy this sentence: I love to learn new things.", "I love to learn new things.")
    ]
    prompt, expected = random.choice(prompts)
    print(f"Task: {prompt}")
    if expected is not None:
        # For copy tasks, get the user's response and compare it
        user_response = input("Type your answer: ")
        score = similarity_score(expected, user_response)
        print(f"Similarity score: {score:.2f}")
        if score >= 0.9:
            print("Great job on copying accurately!")
        else:
            print("There seem to be some errors; please review the sentence.")
    else:
        input("Press Enter when you have completed the task.")
        print("Task completed!")
    print("Great job on the basic writing task!\n")
    
def sentence_writing_test():
    """Sentence construction tasks."""
    print("=== Sentence Construction Test ===")
    prompts = [
        "Complete this sentence: The dog ran _____.",
        "Arrange these words into a sentence: school - to - go - I - love",
        "Write a sentence using the word 'happy'.",
        "Write a sentence about your best friend.",
        "Write a question you would ask a teacher."
    ]
    prompt = random.choice(prompts)
    print(f"Task: {prompt}")
    input("Press Enter when you have completed the task.")
    print("Great job on the sentence construction task!\n")
    
def creative_writing_test():
    """Creative writing tasks."""
    print("=== Creative Writing Test ===")
    prompts = [
        "Write a short story about a lost balloon.",
        "Describe your favorite food in five sentences.",
        "Write a letter to a friend about your day.",
        "Write a story about a magical adventure.",
        "Describe a time when you felt really proud of yourself."
    ]
    prompt = random.choice(prompts)
    print(f"Task: {prompt}")
    input("Press Enter when you have completed the task.")
    print("Great job on the creative writing task!\n")
    
def assess_writing():
    """Conduct the complete writing assessment."""
    print("Let's test your writing skills!")
    basic_writing_test()
    sentence_writing_test()
    creative_writing_test()
    print("Writing assessment complete!")

if __name__ == '__main__':
    assess_writing()
