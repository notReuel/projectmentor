import random

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
    
    if random.random() < 0.3:  # 30% chance of a word problem
        if operation == '+':
            question = f"If you have {a} apples and get {b} more, how many do you have in total?"
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
    """Adaptive math test to determine child's math level."""
    level = 1
    correct = 0
    total = 0
    required_correct = 7  # Increase mastery threshold
    total_questions = 10  # Increase number of questions
    
    print("Let's test your math skills! Solve the problems correctly to advance.")
    
    while level <= 3:
        question, answer = generate_problem(level)
        print(f"Solve: {question}")
        
        try:
            user_answer = float(input("Your answer: "))
            if abs(user_answer - answer) < 0.1:  # Allows slight floating-point errors
                print("Correct!")
                correct += 1
            else:
                print(f"Incorrect! The correct answer is {answer}")
            total += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if total == total_questions:
            if correct >= required_correct:
                level += 1
                print("Great! Let's try harder problems.")
            else:
                break
            correct = 0
            total = 0
    
    return level

if __name__ == "__main__":
    level = get_math_level()
    print(f"Your estimated math level is: {level}")
