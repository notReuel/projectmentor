# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Learner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    reading_level = db.Column(db.Integer, default=1)
    math_level = db.Column(db.Integer, default=1)
    writing_assessment_completed = db.Column(db.Boolean, default=False)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    learner_id = db.Column(db.Integer, db.ForeignKey('learner.id'), nullable=False)
    assessment_type = db.Column(db.String(20))  # e.g., 'reading', 'math'
    score = db.Column(db.Float)
