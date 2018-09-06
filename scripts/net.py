import networkx as nx
import matplotlib.pyplot as plt

# Opening edges file
with open('../data/edges.csv') as edges_file:
    edges_list = edges_file.readlines()[1:]

G = nx.Graph()

nodes = []
edges = []

for edge in edges_list:
    # Splitting instance attributes
    edge_data = edge.split(',')
    # Assigning source and target node
    source = edge_data[0]
    target = edge_data[1]
    repository = edge_data[2]

    # Source and target nodes have not yet been added to the vertex list
    if source not in nodes and target not in nodes:
        # Adding source and target to nodes list
        nodes.append(source)
        nodes.append(target)
        # Creating nodes in graph
        G.add_node(source)
        G.add_node(target)
        # Creating edge
        G.add_edge(source, target, repository=repository)

    # Target node has not yet been added to the vertex list
    elif source in nodes and target not in nodes:
        # Adding target to nodes list
        nodes.append(target)
        # Adding target to graph
        G.add_node(target)
        # Creating edge
        G.add_edge(source, target, repository=repository)
    
    # Source node has not yet been added to the vertex list
    elif source not in nodes and target in nodes:
        # Adding source to nodes list
        nodes.append(source)
        # Adding source to graph
        G.add_node(source)
        # Creating edge
        G.add_edge(source, target, repository=repository)

    # Both have already been added to the vertex list
    else:
        # Creating edge
        G.add_edge(source, target, repository=repository)
    
    
print(G.number_of_nodes())
print(G.number_of_edges())

# Drawing graph
#plt.subplot(121)
nx.draw(G, with_labels=False, font_weight='bold')
plt.show()