import re

def initialize_globals():
    global erdos_network, name_to_id, id_to_name, author_info
    erdos_network = {}
    name_to_id = {}
    id_to_name = {}
    author_info = {}
    current_id = 1  # 从1开始

    # 将Erdős本人映射到ID 0
    erdos_name = "Paul Erdős"
    name_to_id[erdos_name] = 0
    id_to_name[0] = erdos_name
    erdos_network[0] = set()


def read_erdos_file(file_path):
    global erdos_network, name_to_id, id_to_name, author_info
    author_line_pattern = re.compile(r'^(.*?)(\d{4})(?::\s*(\d+))?$')
    
    current_id = max(name_to_id.values()) + 1 if name_to_id else 1

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_author = None
    for line in lines:
        if len(line) == 1:
            continue
        stripped_line = line
        if stripped_line and not stripped_line.startswith('\t'):
            # 这是作者行
            match = author_line_pattern.search(stripped_line)
            if match:
                author_name = match.group(1).strip()
                year = int(match.group(2))
                count = int(match.group(3)) if match.group(3) else 1

                # 检查作者名字后是否有 *
                is_deceased = author_name.endswith('*')
                if is_deceased:
                    author_name = author_name[:-1].strip()

                if author_name not in name_to_id:
                    name_to_id[author_name] = current_id
                    id_to_name[current_id] = author_name
                    current_id += 1

                current_author_id = name_to_id[author_name]
                if current_author_id not in erdos_network:
                    erdos_network[current_author_id] = set()
                current_author = current_author_id

                author_info[current_author_id] = {'year': year, 'count': count, 'deceased': is_deceased}

                # 将作者与Paul Erdős连接
                erdos_network[current_author].add(0)
                erdos_network[0].add(current_author)
        elif stripped_line.startswith('\t'):
            # 这是合作者行
            coauthor_name = stripped_line.strip()
            # 检查合作者名字后是否有 *
            is_deceased = coauthor_name.endswith('*')
            if is_deceased:
                coauthor_name = coauthor_name[:-1].strip()

            if coauthor_name not in name_to_id:
                name_to_id[coauthor_name] = current_id
                id_to_name[current_id] = coauthor_name
                current_id += 1

            coauthor_id = name_to_id[coauthor_name]
            if current_author is not None:
                erdos_network[current_author].add(coauthor_id)
                if coauthor_id not in erdos_network:
                    erdos_network[coauthor_id] = set()
                erdos_network[coauthor_id].add(current_author)

                # 更新合作者信息
                if coauthor_id not in author_info:
                    author_info[coauthor_id] = {'deceased': is_deceased}
                else:
                    author_info[coauthor_id]['deceased'] = is_deceased

# 初始化全局变量
initialize_globals()

file_path = 'erdos1_modified.txt'
read_erdos_file(file_path)

def write_edges_to_file(output_file_path):
    global erdos_network
    with open(output_file_path, 'w') as file:
        for node1, coauthors in erdos_network.items():
            for node2 in coauthors:
                file.write(f"{node1}\t{node2}\n")

# for author_id in list(erdos_network.keys())[:10]:
#     author_name = id_to_name[author_id]
#     coauthor_ids = erdos_network[author_id]
#     coauthor_names = [id_to_name[coauthor_id] for coauthor_id in coauthor_ids]
#     info = author_info.get(author_id, {})
#     print(f"Author: {author_name} (ID: {author_id})")
#     print("Coauthors:", "\n ".join(coauthor_names))
#     print("Info:", info)
#     print()
# 将edge写入新文件
output_file_path = 'erdos_edges.txt'
write_edges_to_file(output_file_path)

print(f"Edges written to {output_file_path}")


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
            
            print(f"Author ID: {author_id},Author Name: {id_to_name[author_id]}, Degree Centrality: {centrality:.4f}")
        print()

# File paths
edge_file_path = 'erdos_edges.txt'
community_file_path = 'erdos_community_map_output.txt'

main(edge_file_path, community_file_path)