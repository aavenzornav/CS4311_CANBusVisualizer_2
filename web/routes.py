from flask import Flask, render_template, request, flash
from web import app 
from . import db
from .forms import create_project_form, create_node
from datetime import datetime
from werkzeug.utils import redirect
#from web import Network
from pyvis.network import Network
import json

#global to create the size if the node mapping square
net = Network(height="1500px", width="100%", bgcolor="#222222", font_color="white")

#list to hold the nodes
node_list = []

#list to hold the information of a project from the database
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
        #to obtain the database information and store them into a list
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

        #infomation that will be posted to create a node with a specific name
        form = create_node(request.form)
        todo_node_name = form.node_name.data
        todo_add_node_to = form.connector.data

        #appending only the user initials for the moment
        #node_list.append(project_info[0])

        file = "web/static/jsonnodes/node_info.json"
        with open(file, "r") as f:
            data = json.load(f)
        print(data)

        #appending the name of the node inputted by the user
        node_list.append(todo_node_name)
        #net.add_node((todo_node_name))

        prev = 0
        i=0
        net.show_buttons()

        for import_node in data:
            name = (import_node["name"])
            #id_num = (thing["id"])
            net.add_node(name)
            # for loop is to add a node inside the node map
            for item in node_list:
                net.add_node(item)
                #to check which node we will connect to, optional
                if todo_add_node_to == name:
                    net.add_edge(name, todo_node_name)
                if todo_add_node_to == node_list[i]:
                    net.add_edge(todo_add_node_to, item)
            '''            for i in range(len(node_list)):
                print(node_list)
                net.add_node(i, label=node_list[i])
                if todo_add_node_to == name:
                    net.add_edge(name, i)
                elif todo_add_node_to == node_list:
                    net.add_edge(todo_node_name, todo_add_node_to)
'''

                    #net.add_edge(name, i)

                #prev += 1
        net.show("web/templates/nodes.html")  # creates a new file from "nodes.html"
        return redirect('can-bus-manager')
    else:
        form = create_node(request.form)
    return render_template('can-bus-manager.html', title='CAN Bus Manager',form = form)

@app.route('/view-traffic')

def view_traffic():
    return render_template('view-traffic.html', title='View Traffic')





