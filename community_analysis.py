import networkx as nx
from collections import defaultdict

def read_edges(file_path):
    edges = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            node1, node2 = map(int, line.strip().split('\t'))
            edges.append((node1, node2))
    return edges

def read_communities(file_path):
    community_map = defaultdict(list)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            node, community = map(int, line.strip().split(': '))
            community_map[community].append(node)
    return community_map

def main(edge_file_path, community_file_path):
    edges = read_edges(edge_file_path)
    community_map = read_communities(community_file_path)
    
    # Create graph
    G = nx.Graph()
    G.add_edges_from(edges)
    
    # Identify the largest communities
    sorted_communities = sorted(community_map.items(), key=lambda x: len(x[1]), reverse=True)
    largest_communities = sorted_communities[:5]
    
    # Analyze each of the largest communities
    for i, (community, nodes) in enumerate(largest_communities, 1):
        subgraph = G.subgraph(nodes)
        degree_centrality = nx.degree_centrality(subgraph)
        top_5_authors = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        
        print(f"Community {i} (Size: {len(nodes)}):")
        for author_id, centrality in top_5_authors:
            print(f"Author ID: {author_id}, Degree Centrality: {centrality:.4f}")
        print()

# File paths
edge_file_path = 'erdos_edges.txt'
community_file_path = 'erdos_community_map_output.txt'

main(edge_file_path, community_file_path)
