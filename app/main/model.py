from flask_sqlalchemy import SQLAlchemy
from app import db

# Create a model for the message history
class MessageHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
      
      
# Create a model for the reminders
class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reminder_time = db.Column(db.String(10), nullable=False)
    medicine_label = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)