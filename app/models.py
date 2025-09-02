# File to structure User and Link data models
# Users e links são classes entidade que armazenarão # será links parte de users?
from datetime import datetime
from . import db


class User(db.Model):
    """Main structure for users"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    links = db.relationship('Link', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def set_username(self, name):
        self.username = name

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password_hash = f"hashed_{password}"
    

class Link(db.Model):
    """Link object"""
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    # Foreign Key that links a Link to a User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='links')

    def __repr__(self):
        return f"<Link {self.title}>"

