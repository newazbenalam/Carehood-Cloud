from flask import session, redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

from app.main.model import Reminder, User
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    # name = session.get('name', '')
    # room = session.get('room', '')
    name = session.get('username')
    room = session.get('username')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room,username=session.get('username'))

@main.route('/chat1')
def chat1():
    """Chat room. The user's name and room must be stored in
    the session."""
    # name = session.get('name', '')
    # room = session.get('room', '')
    name = session.get('username')
    room = session.get('username')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat1.html', name=name, room=room)



@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, "pbkdf2:sha256")
        # print(hashed_password)

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('main.login'))
    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']

        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        # print(password)  # Check the password entered by the user
        # print(user.password)  # Check the hashed password retrieved from the database

        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = username
            session['name'] = username
            session['room'] = username
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'logged_in' in session:
        
        username = session['username']
        return render_template('dashboard.html', username=username)
    return redirect(url_for('main.login'))


@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))

# Route to display the medicine status
@main.route('/todo', methods=['GET'])
def todo():
    reminders = Reminder.query.all()
    return render_template('reminder.html', reminders=reminders, username=session.get('username'))

# Route to handle adding a reminder
@main.route('/todo', methods=['POST'])
def add_reminder():
    reminder_time = request.form['reminderTime']
    medicine_label = request.form['medicineLabel']
    description = request.form['description']

    new_reminder = Reminder(reminder_time=reminder_time, medicine_label=medicine_label, description=description)
    db.session.add(new_reminder)
    db.session.commit()

    return redirect(url_for('main.add_reminder',username=session.get('username')))