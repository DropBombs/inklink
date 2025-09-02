from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    """Create and configurate an instance of the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Associate extensions to the application's instance 
    db.init_app(app)

    # Import and register routes
    with app.app_context():
        import app.auth.routes as routes

        # db.create_all()

    return app
