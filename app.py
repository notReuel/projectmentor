from flask import Flask, render_template, request, redirect, url_for, flash
from assessments.adaptive_reading_assessment import get_reading_level, test_comprehension
from assessments.writing_assessment import assess_writing
from assessments.math_assessment import get_math_level
from utils.analytics import aggregate_results
from utils.learner_profiles import add_or_update_learner, get_learner
from main import start_assessment  # Import the refactored start_assessment function

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Global variables to hold learner data during the session
latest_results = {}
learner_id = None

@app.route('/')
def index():
    return render_template('index.html')  # Your home page template

@app.route('/set_learner', methods=['GET', 'POST'])
def set_learner():
    global learner_id
    if request.method == 'POST':
        learner_id = request.form.get('learner_id')
        if not learner_id:
            flash("Learner ID is required", "error")
            return redirect(url_for('set_learner'))
        flash(f"Learner ID set to: {learner_id}", "success")
        return redirect(url_for('index'))
    return render_template('set_learner.html')

@app.route('/reading')
def reading_assessment():
    try:
        reading_level = get_reading_level()
        flash(f"Your estimated reading level is: {reading_level}", "info")
        # Note: test_comprehension() may need further adaptation to work well in a web environment.
        test_comprehension()
        latest_results['reading_level'] = reading_level
    except Exception as e:
        flash(f"Error during reading assessment: {e}", "error")
    return redirect(url_for('index'))

@app.route('/writing')
def writing_assessment():
    try:
        assess_writing()
        latest_results['writing_assessment_completed'] = True
        flash("Writing assessment completed.", "info")
    except Exception as e:
        flash(f"Error during writing assessment: {e}", "error")
    return redirect(url_for('index'))

@app.route('/math')
def math_assessment():
    try:
        math_level = get_math_level()
        flash(f"Your estimated math level is: {math_level}", "info")
        latest_results['math_level'] = math_level
    except Exception as e:
        flash(f"Error during math assessment: {e}", "error")
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if latest_results:
        analytics_data = aggregate_results()
        return render_template('dashboard.html', analytics=analytics_data)
    flash("No assessment data available yet. Please complete assessments first.", "warning")
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    global learner_id
    if not learner_id:
        flash("Please set your Learner ID first.", "error")
        return redirect(url_for('set_learner'))
    profile_data = get_learner(learner_id)
    return render_template('profile.html', learner_id=learner_id, profile=profile_data)

# ---- New Route for Starting Assessment ----
@app.route('/start_assessment', methods=['GET', 'POST'])
def start_assessment_route():
    global learner_id, latest_results
    if request.method == 'POST':
        learner_id = request.form.get('learner_id')
        if not learner_id:
            flash("Learner ID is required to start assessments.", "error")
            return redirect(url_for('set_learner'))
        # Call the refactored assessment function that runs all tests and returns results.
        data = start_assessment(learner_id)
        # Update the global results (if needed) or simply pass to the template.
        latest_results.update(data.get("results", {}))
        # Optionally, update learner profile as part of start_assessment() already does that.
        return render_template('assessment_results.html', data=data)
    return render_template('start_assessment.html')

if __name__ == '__main__':
    app.run(debug=True)
