from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from assessments.enhanced_reading_assessment import get_reading_level, test_comprehension
from assessments.enhanced_writing_assessment import assess_writing
from assessments.enhanced_math_assessment import get_math_level
from utils.analytics import aggregate_results
from utils.learner_profiles import add_or_update_learner, get_learner, generate_learner_profile
from utils.progress_tracker import save_progress
from forms import RegistrationForm, LoginForm
from utils.auth import register_user, verify_password
# Import your authentication functions if available
from utils.auth import login_manager, get_user  # Ensure you have implemented basic auth functions

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secure_secret_key'  # Replace with a secure key

# ------------------------------
# Database Setup with SQLAlchemy
# ------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ai_tutor.db'  # For development; use PostgreSQL for production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Assuming you have models defined in models.py
with app.app_context():
    # Create all database tables
    from models import Learner, Progress  # Ensure your models are in models.py
    db.create_all()

# ------------------------------
# Authentication Setup (Placeholder)
# ------------------------------
login_manager.init_app(app)
login_manager.login_view = 'login'  # Define your login route accordingly

@login_manager.user_loader
def load_user(user_id):
    """
    Given a user_id, return the corresponding User object.
    """
    return get_user(user_id)

# Global variables to hold session data
latest_results = {}
learner_id = None

# ------------------------------
# Routes
# ------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = register_user(form.email.data, form.password.data)
        if user:
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        else:
            flash("A user with that email already exists.", "error")
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Dummy user lookup by iterating over dummy_users
        user = None
        for u in dummy_users.values():
            if u.email == form.email.data and verify_password(u.password_hash, form.password.data):
                user = u
                break
        if user:
            # Here you would normally log the user in using login_user from Flask-Login.
            flash("Logged in successfully.", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials.", "error")
    return render_template('login.html', form=form)

@app.route('/')
def index():
    return render_template('index.html')  # Home page

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

# New route: Process reading assessment using client-side transcript
@app.route('/process_reading', methods=['POST'])
def process_reading():
    transcript = request.form.get('transcript')
    expected_word = request.form.get('expected_word')
    if not transcript or not expected_word:
        return jsonify({"error": "Missing transcript or expected word."}), 400
    # Import web-based reading assessment processing function
    from assessments.web_reading_assessment import process_reading_assessment
    result = process_reading_assessment(transcript, expected_word)
    return jsonify(result)

# Route for reading assessment (if using server-side for now)
@app.route('/reading')
def reading_assessment():
    try:
        reading_level = get_reading_level()
        flash(f"Your estimated reading level is: {reading_level}", "info")
        # Note: test_comprehension() may need adaptation for a web environment.
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
    # Optionally, generate a summary profile if needed:
    summary = generate_learner_profile(profile_data) if profile_data else {}
    return render_template('profile.html', learner_id=learner_id, profile=profile_data, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
