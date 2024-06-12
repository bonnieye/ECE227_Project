import networkx as nx
import matplotlib.pyplot as plt

def load_graph_from_file(file_path):
    # Create a graph from an edge list file
    G = nx.read_edgelist(file_path, nodetype=int, data=(('weight', float),))
    return G

def apply_label_propagation(G, output_file):
    # Use the Label Propagation algorithm
    communities = list(nx.algorithms.community.label_propagation_communities(G))
    community_map = {node: cid for cid, community in enumerate(communities) for node in community}
    
    # Visualizing the network with its community structure
    pos = nx.spring_layout(G)
    cmap = plt.cm.get_cmap('viridis', len(communities))
    nx.draw_networkx_nodes(G, pos, node_size=40, node_color=[community_map[node] for node in G.nodes()], cmap=cmap)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.savefig(output_file)  
    plt.close()  

    with open('erdos_community_map_output.txt', 'w') as f:
        for node, community in community_map.items():
            f.write(f'{node}: {community}\n')

    return community_map


file_path = 'erdos_edges.txt'  
output_file = 'erdos_label_p_network_communities.png'  
G = load_graph_from_file(file_path)
community_map = apply_label_propagation(G, output_file)
#print("Label Propagation community map:", community_map)
