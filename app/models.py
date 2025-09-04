# File to structure User and Link data models

import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db


class User(db.Model):
    """User entity designed to represent users"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    links = db.relationship('Link', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def _validate_username(self, name):
        if not isinstance(name, str):
            raise ValueError("Username must be a string.")
        if len(name) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        elif len(name) > 80:
            raise ValueError("Username cannot exceed 80 characters.")
    
        return name
    
    def _validate_email(self, email):
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        if len(email) > 120:
            raise ValueError("Email cannot exceed 120 characters.")
        elif len(email) < 3:
            raise ValueError("Email must be at least 3 characters long.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address format.")
        
        return email
    
    def _validate_password(self, password):
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")
        if len(password) < 6:
            raise ValueError("Passwords must be at least 6 characters long.")
        elif len(password) > 32:
            raise ValueError("Passwords cannot exceed 32 characters.")
        
        return generate_password_hash(password)
        

    def set_username(self, name):
        self.username = self._validate_username(name)

    def set_email(self, email):
        self.email = self._validate_email(email)

    def set_password(self, password):
        self.password_hash = self._validate_password(password)
    

class Link(db.Model):
    """Link entity designed to represent user's links"""
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

    def _validate_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if len(title) < 2:
            raise ValueError("Title must be at least 2 characters long.")
        elif len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters.")
        
        return title

    def _validate_url(self, url):
        if not isinstance(url, str):
            raise ValueError("URL must be a string.")
        if len(url) < 3:
            raise ValueError("URL must be at least 2 characters long.")
        elif len(url) > 500:
            raise ValueError("URL cannot exceed 500 characters.")
        if not re.match(r"https?:\/\/w{0,3}\.?[a-zA-Z0-9]{2,}\.([a-zA-Z0-9]{2,})\.?([a-zA-Z0-9]{2,})?", url):
            raise ValueError("Invalid URL format.")
        
        return url

    def set_title(self, title):
        self.title = self._validate_title(title)
    
    def set_url(self, url):
        self.url = self._validate_url(url)
