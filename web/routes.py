from flask import Flask, render_template
from web import app

@app.route('/')
@app.route('/base')

def homepage():
    return render_template('base.html', title='Home')

@app.route('/create-project')

def create_project():
    return render_template('create-project.html', title='Create Project')

@app.route('/open-project')

def open_project():
    return render_template('open-project.html', title='Open Existing Project')

@app.route('/sync-project')

def sync_project():
    return render_template('sync-project.html', title='Sync Project')

@app.route('/archive-project')

def archive_project():
    return render_template('archive-project.html', title='Archive Project')

@app.route('/can-bus-manager')

def can_bus_manager():
    return render_template('can-bus-manager.html', title='CAN Bus Manager')


