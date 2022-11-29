from flask import Flask, render_template, request, flash
from web import app 
from . import db
from .forms import create_project_form, create_node
from datetime import datetime
from werkzeug.utils import redirect
#from web import Network
from pyvis.network import Network

net = Network(height="1500px", width="100%", bgcolor="#222222", font_color="white")

node_list = []
project_info =[]
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
    todos.append(todo)
    return render_template('node-map1.html', title='Open Existing Project', todos=todos)

#create project will be stored in mongo db
@app.route('/manage-project', methods = ("POST", "GET"))
def manage_project():
   
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
        return redirect('/')
    else:
        form = create_project_form(request.form)
    return render_template('manage-project.html', title='Create Project', form=form)


@app.route('/sync-project')

def sync_project():
    return render_template('sync-project.html', title='Sync Project')

@app.route('/archive-project')

def archive_project():
    return render_template('archive-project.html', title='Archive Project')

@app.route("/node_map", methods = ("POST", "GET"))
def node_map():
    print("enter")
    #print(node_list)
    #mapper(node_list)
    return render_template('Network.py', title='CAN Bus Map')
@app.route('/can-bus-manager', methods = ("POST", "GET"))
def can_bus_manager():
    if request.method == "POST":
        #to obtain the database information
        info = db.project.find_one({"user_initials": "admin"})
        user = info["user_initials"]
        event = info["event_name"]
        can_id = info["can_connector_id"]
        vehicle_id = info["vehicle id"]
        baud_rate = info["baud_rate"]

        project_info.append(user)
        project_info.append(event)
        project_info.append(can_id)
        project_info.append(vehicle_id)
        project_info.append(baud_rate)

        form = create_node(request.form)
        todo_node_name = form.node_name.data
        node_list.append(todo_node_name)
        #user = "admin"
        #proj = [] #todos

        i=0
        todos = []
        # todo = db.project.find_one({"event_name": "Proj1"})

        #for todo in db.project.find({"user_initials": "admin"}):

            #print(todo)
            #todos.append(todo)
            #print("un",todos)


        #print("befor ret")
        #Network.mapper(node_list)
        print("test")
        #net = Network(height="1500px", width="100%", bgcolor="#222222", font_color="white")
        prev = 0
        net.show_buttons()
        #net.show_buttons(filter_=["edges"])
        for i in range(len(node_list)):
            print(i)
            net.add_node(i, label=node_list[i])
            if (i == 0):
                continue
            else:
                net.add_edge(prev, i)
                prev += 1

        net.show("web/templates/nodes.html")  # creates a new file from "nodes.html"
        # display(HTML("nodes.html"))
        return redirect('can-bus-manager')
    else:
        form = create_node(request.form)
    return render_template('can-bus-manager.html', title='CAN Bus Manager',form = form)

@app.route('/view-traffic')

def view_traffic():
    return render_template('view-traffic.html', title='View Traffic')





