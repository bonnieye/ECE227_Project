import networkx as nx

# Create a new graph
G = nx.Graph()

# Load data from file
with open('erdos_edges.txt', 'r') as file:
    for line in file:
        nodes = line.strip().split()
        G.add_edge(int(nodes[0]), int(nodes[1]))

# Function to find the diameter of each connected component
def get_graph_diameters(graph):
    diameters = []
    for component in nx.connected_components(graph):
        subgraph = graph.subgraph(component)
        diameter = nx.diameter(subgraph)
        diameters.append(diameter)
    return diameters

# Calculate diameters of all connected components
component_diameters = get_graph_diameters(G)
max_diameter = max(component_diameters) if component_diameters else None

print("Diameters of all components:", component_diameters)
print("Maximum diameter (Diameter of the graph):", max_diameter)
