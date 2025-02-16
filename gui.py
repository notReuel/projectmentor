import tkinter as tk
from tkinter import messagebox
import threading
import subprocess

def run_assessments():
    """
    Runs the main.py script in a subprocess and captures its output.
    """
    try:
        # Run main.py and capture its output (make sure to adjust the Python executable path if needed)
        result = subprocess.run(["python", "enhanced_main.py"], capture_output=True, text=True)
        # Insert the captured output into the text widget
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_assessment_thread():
    """
    Starts the assessment process in a separate thread to avoid freezing the GUI.
    """
    thread = threading.Thread(target=run_assessments)
    thread.start()

# Create the main Tkinter window
root = tk.Tk()
root.title("AI Tutor MVP")

# Create a frame for the welcome message and button
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

welcome_label = tk.Label(frame, text="Welcome to the AI Tutor MVP!", font=("Arial", 16))
welcome_label.pack(pady=(0, 20))

start_button = tk.Button(frame, text="Start Assessment", font=("Arial", 14), command=start_assessment_thread)
start_button.pack(pady=(0, 20))

# Create a text widget to display the output from the assessments
output_text = tk.Text(root, wrap=tk.WORD, height=20, width=80)
output_text.pack(padx=20, pady=20)

# Start the GUI event loop
root.mainloop()

