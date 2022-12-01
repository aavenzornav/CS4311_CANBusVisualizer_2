from flask import Flask, render_template, request, flash
from web import app
import os
import subprocess
from . import db
from .forms import create_project_form, create_node, sync_form
from datetime import datetime
from werkzeug.utils import redirect
#from web import Network
import networkx as nx
from pyvis.network import Network
import json

#global to create the size if the node mapping square
#creating networkx for rendering through pyvis
netGraph = nx.Graph()
net = Network(height="1000px", width="1000px", bgcolor="#222222", font_color="white")

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
    projRecord = []
    for record in db.project.find().sort("user_initials", -1):
        projRecord["_id"] = str(projRecord["_id"])
        projRecord.append(record)
    #info = db.project.find()
    return render_template('open-project.html', title='Open Existing Project', todos=projRecord)
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
        user_initials = form.user_initials.data
        event_name = form.event_name.data
        can_connector_id = form.can_connector_id.data
        vehicle_id = form.vehicle_id.data
        baud_rate = form.baud_rate.data
        can_dbc = form.can_dbc.data


        db.project.insert_one({
            "user_initials": user_initials,
            "event_name": event_name,
            "can_connector_id": can_connector_id,
            "vehicle id": vehicle_id,
            "baud_rate": baud_rate,
            "can_dbc": can_dbc
        })
        return redirect('/')
    else:
        form = create_project_form(request.form)
    return render_template('manage-project.html', title='Create Project', form=form)


@app.route('/sync-project', methods = ("POST", "GET"))
def sync_project():


    if request.method == "GET":
        print("hello")
        form = sync_form(request.form)
        argstwo = ["rsync" , 'web/src/j1939_1.dbc' , 'web/dest/hello.dbc']
        subprocess.call(argstwo);
        return render_template('sync-project.html', title='Sync Project', srcPath='/web/lib/projects', form=form)

    else:
        form = sync_form(request.form)
        return render_template('sync-project.html', title='Sync Project', srcPath='/web/lib/projects', form=form)

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
        node_name = form.node_name.data
        add_node_to = form.connector.data

        #appending only the user initials for the moment
        #node_list.append(project_info[0])

        file = "web/static/jsonnodes/node_info.json"
        with open(file, "r") as f:
            data = json.load(f)
        print(data)

        #appending the name of the node inputted by the user
        node_list.append(node_name)
        #net.add_node((todo_node_name))

        prev = 0
        i=0

        for import_node in data:
            name = (import_node["name"])
            #id_num = (thing["id"])
            netGraph.add_node(name)
            # for loop is to add a node inside the node map
            for item in node_list:
                netGraph.add_node(item)
                #to check which node we will connect to, optional
                if add_node_to == name:
                    netGraph.add_edge(name, node_name)
                if add_node_to == node_list[i]:
                    netGraph.add_edge(add_node_to, item)
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
        net.from_nx(netGraph)
        #net.show_buttons()
        net.show("web/templates/nodes.html")  # creates a new file from "nodes.html"
        return redirect('can-bus-manager')
    else:
        form = create_node(request.form)
    return render_template('can-bus-manager.html', title='CAN Bus Manager',form = form)

@app.route('/view-traffic')

def view_traffic():
    return render_template('view-traffic.html', title='View Traffic')

@app.route('/tags')

def tag_nodes():
    return render_template('tag_nodes.html', title='Sync Project', nID='0x7E5', blStatus = 'False')




