from pyvis.network import Network
import json


#testing to make the mapping of nodes without using data
def map(node_list):
    print("test")
    net = Network(height = "1500px", width = "100%", bgcolor = "#222222", font_color="white")
    for i in range(node_list):
        net.add_node(i, label = "Node"+i)
        #net.add_edge(i,2)
    net.show("nodes.html") #creates a new file from "nodes.html"
        #display(HTML("nodes.html"))

#map()