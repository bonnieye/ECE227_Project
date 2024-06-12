import networkx as nx
import json


file_path = 'erdos_edges.txt'
G = nx.read_edgelist(file_path, create_using=nx.Graph(), nodetype=int)


degree_centrality = nx.degree_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)


num_top_nodes = int(0.1 * G.number_of_nodes())

top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:num_top_nodes]
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:num_top_nodes]
top_eigenvector = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:num_top_nodes]


centrality_data = {
    "degree_centrality": degree_centrality,
    "betweenness_centrality": betweenness_centrality,
    "eigenvector_centrality": eigenvector_centrality,
    "top_degree": top_degree,
    "top_betweenness": top_betweenness,
    "top_eigenvector": top_eigenvector
}

with open('erdos_centrality_results.json', 'w') as f:
    json.dump(centrality_data, f, indent=4)


print("Top 10% nodes by Degree Centrality:")
for node, centrality in top_degree:
    print(f"Node: {node}, Degree Centrality: {centrality}")

print("\nTop 10% nodes by Betweenness Centrality:")
for node, centrality in top_betweenness:
    print(f"Node: {node}, Betweenness Centrality: {centrality}")

print("\nTop 10% nodes by Eigenvector Centrality:")
for node, centrality in top_eigenvector:
    print(f"Node: {node}, Eigenvector Centrality: {centrality}")
