from graph_tool.all import *

# Creating graph (undirected)
g = Graph(directed=False)

# Opening edges file
with open('../data/edges.csv') as edges_file:
    edges_list = edges_file.readlines()[1:]

nodes = []
edges = []

class MyClass(object):
    def __init__(self, title):
        self.title = title

for edge in edges_list:
    edge_data = edge.split(',')

    source = edge_data[0]
    target = edge_data[1]
    '''
    repository = edge_data[2]
    stars = edge_data[3]
    forks = edge_data[4]
    issues = edge_data[5]
    size = edge_data[6]
    language = edge_data[7]
    '''

    if source not in nodes:
        # Adding node to nodes list
        nodes.append(source)
        # Creating node in graph
        v = g.add_vertex()

        my_obj = MyClass(source)
        v_prop = g.new_vertex_property('object')
        v_prop[v] = my_obj
        
    
    if target not in nodes:
        # Adding node to nodes list
        nodes.append(target)
        # Creating node in graph
        v = g.add_vertex()

        my_obj = MyClass(target)
        v_prop = g.new_vertex_property('object')
        v_prop[v] = my_obj

v_prop = g.new_vertex_property('object')
for vertex in g.vertices():
    print(v_prop[vertex].title)

# graph_draw(g)