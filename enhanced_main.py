import tkinter as tk
from tkinter import messagebox, simpledialog
from assessments.enhanced_reading_assessment import get_reading_level, test_comprehension
from assessments.enhanced_writing_assessment import assess_writing
from assessments.enhanced_math_assessment import get_math_level
from utils.dashboard import open_dashboard
from utils.learner_profiles import get_learner  # For viewing profiles

# Global dictionary to hold the latest assessment results
latest_results = {}
learner_id = None  # Global variable for the learner ID

def prompt_learner_id():
    global learner_id
    learner_id = simpledialog.askstring("Learner ID", "Enter your Learner ID:")
    if not learner_id:
        messagebox.showerror("Input Error", "Learner ID is required.")
    else:
        messagebox.showinfo("Learner ID", f"Learner ID set to: {learner_id}")

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

def show_analytics():
    from utils.analytics import aggregate_results
    analytics_data = aggregate_results()
    
    if not analytics_data:
        messagebox.showinfo("Analytics", "No data available.")
        return
    
    analytics_window = tk.Toplevel(root)
    analytics_window.title("Learner Analytics")
    
    tk.Label(analytics_window, text="Learner Performance Analytics", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(analytics_window, text=f"Total Assessments: {analytics_data.get('total_assessments', 0)}", font=("Arial", 12)).pack(pady=5)
    tk.Label(analytics_window, text=f"Average Reading Level: {analytics_data.get('avg_reading_level', 0):.2f}", font=("Arial", 12)).pack(pady=5)
    tk.Label(analytics_window, text=f"Average Math Level: {analytics_data.get('avg_math_level', 0):.2f}", font=("Arial", 12)).pack(pady=5)

def show_learner_profile():
    global learner_id
    if not learner_id:
        messagebox.showwarning("Learner Profile", "Please set your Learner ID first.")
        return
    profile = get_learner(learner_id)
    profile_window = tk.Toplevel(root)
    profile_window.title("Learner Profile")
    
    if profile:
        tk.Label(profile_window, text=f"Learner ID: {learner_id}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(profile_window, text=f"Profile Data: {profile}", font=("Arial", 12)).pack(pady=5)
    else:
        tk.Label(profile_window, text="No profile data available for this learner.", font=("Arial", 12)).pack(pady=10)

def run_tests():
    messagebox.showinfo("Tests", "Running tests... (Tests are executed externally via your test suite.)")

def exit_app():
    root.quit()

# Tkinter UI Setup
root = tk.Tk()
root.title("Enhanced AI Tutor MVP")

tk.Label(root, text="Welcome to the Enhanced AI Tutor MVP", font=("Arial", 16, "bold")).pack(pady=15)

tk.Button(root, text="Set Learner ID", command=prompt_learner_id, width=30).pack(pady=5)
tk.Button(root, text="Run Reading Assessment", command=run_reading_assessment, width=30).pack(pady=5)
tk.Button(root, text="Run Writing Assessment", command=run_writing_assessment, width=30).pack(pady=5)
tk.Button(root, text="Run Math Assessment", command=run_math_assessment, width=30).pack(pady=5)
tk.Button(root, text="View Dashboard", command=show_dashboard, width=30).pack(pady=5)
tk.Button(root, text="View Analytics", command=show_analytics, width=30).pack(pady=5)
tk.Button(root, text="View Learner Profile", command=show_learner_profile, width=30).pack(pady=5)
tk.Button(root, text="Run Tests", command=run_tests, width=30).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, width=30).pack(pady=10)

root.mainloop()
