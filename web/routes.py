from flask import Flask, render_template
from web import app

@app.route('/')
@app.route('/base')

def homepage():
    return render_template('base.html')