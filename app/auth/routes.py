# File to organize and manage routes
from flask import current_app as app
from flask import render_template

# Inklink main page
@app.route('/')
def index():
    return f"<h1> Inklink </h1>"

# Public link page for users
@app.route('/<username>')
def user_page(username):
    # Future link retrieval logic
    return f"<h1> Página de {username}</h1>"

# Home page of logged users
@app.route('/dashboard')
def dashboard():
    # Future logic for logged users links
    return render_template('dashboard.html')
