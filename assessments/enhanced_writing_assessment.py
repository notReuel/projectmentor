import random
from difflib import SequenceMatcher
import tkinter as tk
from tkinter import simpledialog, messagebox

def similarity_score(expected, actual):
    """Returns a similarity ratio between expected and actual text."""
    return SequenceMatcher(None, expected.lower(), actual.lower()).ratio()

def get_user_input(prompt):
    """Uses a Tkinter dialog to get user input."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    answer = simpledialog.askstring("Input", prompt)
    root.destroy()
    return answer

def basic_writing_test():
    """Basic writing tasks with GUI dialogs for input and output."""
    prompts = [
        ("Write the alphabet from A to Z.", None),
        ("Copy this sentence: The cat is on the mat.", "The cat is on the mat."),
        ("Write your name three times.", None),
        ("Write the numbers 1 to 20 in words.", None),
        ("Copy this sentence: I love to learn new things.", "I love to learn new things.")
    ]
    prompt, expected = random.choice(prompts)
    messagebox.showinfo("Basic Writing Test", f"Task: {prompt}")
    
    if expected is not None:
        user_response = get_user_input("Type your answer:")
        score = similarity_score(expected, user_response) if user_response else 0
        result_msg = f"Similarity score: {score:.2f}\n"
        result_msg += "Great job on copying accurately!" if score >= 0.9 else "There seem to be some errors; please review the sentence."
        messagebox.showinfo("Result", result_msg)
    else:
        messagebox.showinfo("Task Completed", "Task completed!")
    
def sentence_writing_test():
    """Sentence construction tasks with GUI dialogs."""
    prompts = [
        "Complete this sentence: The dog ran _____.",
        "Arrange these words into a sentence: school - to - go - I - love",
        "Write a sentence using the word 'happy'.",
        "Write a sentence about your best friend.",
        "Write a question you would ask a teacher."
    ]
    prompt = random.choice(prompts)
    messagebox.showinfo("Sentence Writing Test", f"Task: {prompt}")
    get_user_input("When you've completed the task, press OK.")
    messagebox.showinfo("Task Completed", "Great job on the sentence construction task!")
    
def creative_writing_test():
    """Creative writing tasks with GUI dialogs."""
    prompts = [
        "Write a short story about a lost balloon.",
        "Describe your favorite food in five sentences.",
        "Write a letter to a friend about your day.",
        "Write a story about a magical adventure.",
        "Describe a time when you felt really proud of yourself."
    ]
    prompt = random.choice(prompts)
    messagebox.showinfo("Creative Writing Test", f"Task: {prompt}")
    get_user_input("When you've completed the task, press OK.")
    messagebox.showinfo("Task Completed", "Great job on the creative writing task!")
    
def assess_writing():
    """Conduct the complete writing assessment using GUI elements."""
    basic_writing_test()
    sentence_writing_test()
    creative_writing_test()
    messagebox.showinfo("Writing Assessment", "Writing assessment complete!")
    
if __name__ == '__main__':
    assess_writing()
