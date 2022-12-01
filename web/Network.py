from pyvis.network import Network
import json


#testing to make the mapping of nodes without using data
def mapper(node_list):
    print("test")
    net = Network(height = "1500px", width = "100%", bgcolor = "#222222", font_color="white")
    prev = 0
    for i in range(len(node_list)):
        print(i)
        net.add_node(i, label = node_list[i])
        if(i==0):
            continue
        else:
            net.add_edge(prev,i)
            prev+=1
    net.show("web/templates/nodes.html") #creates a new file from "nodes.html"
        #display(HTML("nodes.html"))

#map()