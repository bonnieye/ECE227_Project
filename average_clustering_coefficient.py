import networkx as nx

def read_edges(file_path):
    edges = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            node1, node2 = map(int, line.strip().split('\t'))
            edges.append((node1, node2))
    return edges

def main(file_path):
    edges = read_edges(file_path)
    
    G = nx.Graph()
    
    G.add_edges_from(edges)
    
    num_nodes = G.number_of_nodes()
    
    num_edges = G.number_of_edges()
    
    avg_clustering_coefficient = nx.average_clustering(G)
    
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Average Clustering Coefficient: {avg_clustering_coefficient:.4f}")

file_path = 'erdos_edges.txt'
main(file_path)
