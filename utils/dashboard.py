# utils/dashboard.py
import tkinter as tk
from tkinter import ttk
from utils.analytics import aggregate_results
from utils.progress_tracker import load_progress
from utils.lesson_planner import generate_lesson_plan

def open_dashboard(results):
    dashboard = tk.Toplevel()
    dashboard.title("Parental Dashboard")

    # Create Notebook widget for tabbed interface
    notebook = ttk.Notebook(dashboard)
    notebook.pack(fill='both', expand=True)

    # Tab 1: Assessment Progress
    progress_frame = ttk.Frame(notebook)
    notebook.add(progress_frame, text="Assessment Progress")

    progress_text = tk.Text(progress_frame, wrap=tk.WORD, width=60, height=20)
    progress_text.pack(fill='both', expand=True)

    progress_data = load_progress()
    progress_text.insert(tk.END, "Assessment Progress:\n\n")
    if progress_data:
        for entry in progress_data:
            progress_text.insert(tk.END, f"{entry}\n")
    else:
        progress_text.insert(tk.END, "No progress data available.\n")

    # Tab 2: Aggregated Analytics
    analytics_frame = ttk.Frame(notebook)
    notebook.add(analytics_frame, text="Aggregated Analytics")

    analytics_text = tk.Text(analytics_frame, wrap=tk.WORD, width=60, height=20)
    analytics_text.pack(fill='both', expand=True)
    aggregated = aggregate_results()
    analytics_text.insert(tk.END, "Aggregated Analytics:\n\n")
    analytics_text.insert(tk.END, f"Total Assessments: {aggregated.get('total_assessments', 'N/A')}\n")
    analytics_text.insert(tk.END, f"Average Reading Level: {aggregated.get('avg_reading_level', 0):.2f}\n")
    analytics_text.insert(tk.END, f"Average Math Level: {aggregated.get('avg_math_level', 0):.2f}\n")

    # Tab 3: Personalized Lesson Plan
    lesson_frame = ttk.Frame(notebook)
    notebook.add(lesson_frame, text="Lesson Plan")

    lesson_text = tk.Text(lesson_frame, wrap=tk.WORD, width=60, height=20)
    lesson_text.pack(fill='both', expand=True)
    plan = generate_lesson_plan(results)
    lesson_text.insert(tk.END, "Personalized Lesson Plan:\n\n")
    lesson_text.insert(tk.END, f"Total Hours: {plan.get('total_hours', 'N/A')}\n")
    lesson_text.insert(tk.END, f"Reading Hours: {plan.get('reading_hours', 'N/A')}\n")
    lesson_text.insert(tk.END, f"Writing Hours: {plan.get('writing_hours', 'N/A')}\n")
    lesson_text.insert(tk.END, f"Math Hours: {plan.get('math_hours', 'N/A')}\n")

    # You can add additional tabs here (e.g., Gamification, Learner Profiles, etc.)

    dashboard.mainloop()

if __name__ == "__main__":
    # For testing purposes, we pass a sample results dict.
    sample_results = {"reading_level": 2, "math_level": 2, "writing_assessment_completed": True}
    root = tk.Tk()
    root.withdraw()
    open_dashboard(sample_results)
