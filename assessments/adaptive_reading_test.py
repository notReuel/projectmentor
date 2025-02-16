import random
import speech_recognition as sr
import tkinter as tk
from tkinter import simpledialog, messagebox

# Sample words for different reading levels
LEVEL_1 = ["cat", "dog", "sun", "big", "red"]
LEVEL_2 = ["happy", "garden", "pencil", "tiger", "purple"]
LEVEL_3 = ["elephant", "yesterday", "beautiful", "umbrella", "excited"]

# Sample comprehension questions
COMPREHENSION_QUESTIONS = {
    "cat": "What animal says 'meow'?",
    "dog": "What pet is known as man's best friend?",
    "sun": "What gives us light during the day?",
    "happy": "What is the opposite of sad?",
    "garden": "Where do flowers and vegetables grow?",
    "elephant": "Which animal has a trunk?",
}

def get_reading_level():
    """Enhanced reading test using speech recognition and GUI dialogs."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    levels = [LEVEL_1, LEVEL_2, LEVEL_3]
    current_level = 0
    correct = 0
    total = 0
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    messagebox.showinfo("Reading Assessment", "Let's test your reading! I will show a word and you will repeat it aloud.")
    
    while current_level < len(levels):
        word = random.choice(levels[current_level])
        messagebox.showinfo("Reading Task", f"Please say the following word:\n\n{word}")
        
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=1.5)
            try:
                audio = recognizer.listen(source, timeout=5)
                transcription = recognizer.recognize_google(audio).lower()
                messagebox.showinfo("Speech Recognition", f"You said: {transcription}")
                if transcription == word:
                    correct += 1
                total += 1
            except sr.UnknownValueError:
                messagebox.showwarning("Speech Recognition", "I couldn't understand you. Let's try another word.")
            except sr.RequestError:
                messagebox.showerror("Speech Recognition", "Speech recognition service is unavailable.")
        
        # After 5 words, decide whether to advance
        if total == 5:
            if correct >= 3:
                current_level += 1
                messagebox.showinfo("Progress", "Great job! Let's try harder words.")
            else:
                break
            correct = 0
            total = 0
    
    root.destroy()
    # Return a level from 1 (beginner) to 3 (advanced)
    return current_level + 1

def test_comprehension():
    """Enhanced comprehension test using GUI dialogs."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Comprehension Test", "Now, let's test your understanding of words.")
    score = 0
    total = 0
    for word, question in COMPREHENSION_QUESTIONS.items():
        answer = simpledialog.askstring("Comprehension Question", question)
        if answer and word in answer.lower():
            messagebox.showinfo("Result", "Correct!")
            score += 1
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer involves '{word}'.")
        total += 1
    messagebox.showinfo("Comprehension Score", f"Your comprehension score: {score}/{total}")
    root.destroy()

if __name__ == "__main__":
    level = get_reading_level()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Reading Level", f"Your estimated reading level is: {level}")
    test_comprehension()
