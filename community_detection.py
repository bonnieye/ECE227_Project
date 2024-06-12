import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain

def load_graph_from_file(file_path):
    G = nx.read_edgelist(file_path, nodetype=int, data=(('weight', float),))
    return G

def apply_louvain(G, output_file):
    partition = community_louvain.best_partition(G)

    pos = nx.spring_layout(G)
    cmap = plt.cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.savefig(output_file)  
    plt.close()  
    return partition

file_path = 'erdos_edges.txt'  
output_file = 'erdos_network_visualization.png'  
G = load_graph_from_file(file_path)
partition = apply_louvain(G, output_file)
#print("Louvain partition:", partition)
