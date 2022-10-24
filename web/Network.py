from pyvis.network import Network
import json


#testing to make the mapping of nodes without using data
def map():
    net = Network(height = "1500px", width = "100%", bgcolor = "#222222", font_color="white")
    net.add_node(1, label = "Node 1")
    net.add_node(2)
    net.add_edge(1,2)
    net.show("nodes.html") #creates a new file from "nodes.html"
    #display(HTML("nodes.html"))

map()