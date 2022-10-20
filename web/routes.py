from flask import Flask, render_template, request, flash, redirect,url_for
from web import app 
from . import mongodb_client
from .forms import create_project_form
from datetime import datetime
#from werkzeug.utils import redirect
import sqlalchemy

@app.route('/')
def homepage():
    return render_template('base.html', title='Home')

#create project will be stored in mongo db
@app.route('/manage-project', methods = ["POST", "GET"])
def manage_project():
    if request.method == "POST":
        todo_user_initials = request.form["user_initials"]
        todo_event_name = request.form["event_name"]
        todo_can_connector_id = request.form["can_connector_id"]
        todo_vehicle_id = request.form["vehicle_id"]
        todo_baud_rate = request.form["baud_rate"]
        todo_can_dbc = request.form["can_dbc"]
        #flash("set project successful")

        return redirect(url_for("user", usr = todo_user_initials))

        
    else:
        return render_template('manage-project.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



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

@app.route('/node-map1')
def node_map1():
        return render_template('node-map1.html', title='Node Map')



