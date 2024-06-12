import json


file_path = 'erdos_centrality_results.json'
with open(file_path, 'r') as f:
    centrality_data = json.load(f)


degree_centrality = centrality_data['top_degree']
betweenness_centrality = centrality_data['top_betweenness']


top_degree_set = set(node for node, centrality in degree_centrality)
top_betweenness_set = set(node for node, centrality in betweenness_centrality)


overlap_nodes = top_degree_set.intersection(top_betweenness_set)
overlap_count = len(overlap_nodes)


overlap_nodes_file = 'erdos_edges_overlap_nodes.json'
with open(overlap_nodes_file, 'w') as f:
    json.dump(list(overlap_nodes), f, indent=4)

print(f"Number of nodes in the top 10% for both degree and betweenness centrality: {overlap_count}")
print(f"Overlap nodes have been saved to {overlap_nodes_file}")
