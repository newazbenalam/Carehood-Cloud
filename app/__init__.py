from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__, static_url_path='/static')
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql:12345@localhost:3306/carehood'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



def create_app(debug=False):
    """Create an application."""
    app.debug = debug

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    with app.app_context():
        db.create_all()

    socketio.init_app(app)
    return app

