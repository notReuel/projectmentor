import tkinter as tk
from tkinter import messagebox
from assessments.enhanced_reading_assessment import get_reading_level, test_comprehension
from assessments.enhanced_writing_assessment import assess_writing
from assessments.enhanced_math_assessment import get_math_level
from utils.dashboard import open_dashboard

# Global dictionary to hold the latest assessment results
latest_results = {}

def run_reading_assessment():
    try:
        reading_level = get_reading_level()
        messagebox.showinfo("Reading Assessment", f"Your estimated reading level is: {reading_level}")
        test_comprehension()
        latest_results["reading_level"] = reading_level
    except Exception as e:
        messagebox.showerror("Error", f"Error during reading assessment: {e}")

def run_writing_assessment():
    try:
        assess_writing()
        latest_results["writing_assessment_completed"] = True
    except Exception as e:
        messagebox.showerror("Error", f"Error during writing assessment: {e}")

def run_math_assessment():
    try:
        math_level = get_math_level()
        messagebox.showinfo("Math Assessment", f"Your estimated math level is: {math_level}")
        latest_results["math_level"] = math_level
    except Exception as e:
        messagebox.showerror("Error", f"Error during math assessment: {e}")

def show_dashboard():
    if latest_results:
        open_dashboard(latest_results)
    else:
        messagebox.showwarning("Dashboard", "No assessment data available yet. Please complete assessments first.")

def show_main_menu():
    root = tk.Tk()
    root.title("Enhanced AI Tutor MVP")

    title_label = tk.Label(root, text="Welcome to the Enhanced AI Tutor MVP", font=("Arial", 16))
    title_label.pack(pady=15)

    btn_reading = tk.Button(root, text="Run Reading Assessment", font=("Arial", 12),
                            command=run_reading_assessment, width=30)
    btn_reading.pack(pady=10)

    btn_writing = tk.Button(root, text="Run Writing Assessment", font=("Arial", 12),
                            command=run_writing_assessment, width=30)
    btn_writing.pack(pady=10)

    btn_math = tk.Button(root, text="Run Math Assessment", font=("Arial", 12),
                            command=run_math_assessment, width=30)
    btn_math.pack(pady=10)

    btn_dashboard = tk.Button(root, text="View Dashboard", font=("Arial", 12),
                            command=show_dashboard, width=30)
    btn_dashboard.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", font=("Arial", 12),
                            command=root.quit, width=30)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    show_main_menu()
