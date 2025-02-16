import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_problem(level):
    """Generate a math problem based on difficulty level, including word problems."""
    if level == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
        operation = random.choice(['+', '-'])
        if operation == '-' and a < b:
            a, b = b, a  # Ensure no negative results
    elif level == 2:
        a, b = random.randint(10, 50), random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        if operation == '-' and a < b:
            a, b = b, a
    else:
        a, b = random.randint(10, 100), random.randint(2, 10)
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '-' and a < b:
            a, b = b, a
        if operation == '/':
            a = a - (a % b)  # Ensure exact division
    
    # 30% chance to generate a word problem
    if random.random() < 0.3:
        if operation == '+':
            question = f"If you have {a} apples and get {b} more, how many do you have?"
        elif operation == '-':
            question = f"You have {a} candies and give away {b}. How many do you have left?"
        elif operation == '*':
            question = f"A box has {a} toys. If you buy {b} boxes, how many toys do you have?"
        else:
            question = f"You divide {a} chocolates among {b} friends. How many does each get?"
    else:
        question = f"{a} {operation} {b}"
    
    answer = eval(f"{a} {operation} {b}")
    return question, answer

def get_math_level():
    """Enhanced math test using GUI dialogs."""
    root = tk.Tk()
    root.withdraw()
    level = 1
    correct = 0
    total = 0
    required_correct = 7  # Mastery threshold
    total_questions = 10
    
    messagebox.showinfo("Math Assessment", "Let's test your math skills! Solve the problems correctly to advance.")
    
    while level <= 3:
        question, answer = generate_problem(level)
        user_input = simpledialog.askstring("Math Problem", f"Solve: {question}")
        try:
            user_answer = float(user_input)
            if abs(user_answer - answer) < 0.1:
                messagebox.showinfo("Result", "Correct!")
                correct += 1
            else:
                messagebox.showinfo("Result", f"Incorrect! The correct answer is {answer}.")
            total += 1
        except (ValueError, TypeError):
            messagebox.showwarning("Input Error", "Invalid input. Please enter a number.")
            continue
        
        # After total_questions, decide if we should advance to the next level
        if total == total_questions:
            if correct >= required_correct:
                level += 1
                messagebox.showinfo("Progress", "Great! Let's try harder problems.")
            else:
                break
            correct = 0
            total = 0
    
    root.destroy()
    return level

if __name__ == "__main__":
    level = get_math_level()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Math Level", f"Your estimated math level is: {level}")
