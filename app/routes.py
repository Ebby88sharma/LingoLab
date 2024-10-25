from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='languages.png'))

