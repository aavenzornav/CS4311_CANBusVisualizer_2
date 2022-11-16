from flask import Flask, render_template, request, flash
from web import app 
from . import db
from .forms import create_project_form
from datetime import datetime
from werkzeug.utils import redirect


@app.route('/')
def homepage():
    return render_template('base.html', title='Home')

@app.route('/open-project')
def open_project():
    #same as node-map1 method;
    #this will make it possible to retrieve ALL the collections in the project db
    todos = []
    for todo in db.project.find().sort("user_initials", -1):
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
    #info = db.project.find()
    return render_template('open-project.html', title='Open Existing Project', todos = todos)
@app.route('/node-map1')
def node_map1():
    todos = []
    todo = db.project.find_one({"event_name":  "Proj1"})
    # info = db.project.find()
    todos.append(todo)
    return render_template('node-map1.html', title='Open Existing Project', todos=todos)

#create project will be stored in mongo db
@app.route('/create-project', methods = ("POST", "GET"))
def create_project():
   
    if request.method == "POST":
        form = create_project_form(request.form)
        todo_user_initials = form.user_initials.data
        todo_event_name = form.event_name.data
        todo_can_connector_id = form.can_connector_id.data
        todo_vehicle_id = form.vehicle_id.data
        todo_baud_rate = form.baud_rate.data
        todo_can_dbc = form.can_dbc.data


        db.project.insert_one({
            "user_initials": todo_user_initials,
            "event_name": todo_event_name,
            "can_connector_id": todo_can_connector_id,
            "vehicle id": todo_vehicle_id,
            "baud_rate": todo_baud_rate,
            "can_dbc": todo_can_dbc
        })
        flash("user initials", "event name")
        return redirect('/')
    else:
        form = create_project_form()
    #print(db.project.find_one())
    return render_template('create-project.html', title='Create Project', form=form)


@app.route('/sync-project')

def sync_project():
    return render_template('sync-project.html', title='Sync Project')

@app.route('/archive-project')

def archive_project():
    return render_template('archive-project.html', title='Archive Project')

@app.route('/can-bus-manager')

def can_bus_manager():
    return render_template('can-bus-manager.html', title='CAN Bus Manager')






