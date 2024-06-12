import numpy as np
import matplotlib.pyplot as plt

def read_edge_list(filename):
    degrees = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                node1, node2 = map(int, line.strip().split())
                if node1 != node2:  # Assuming no self-loops
                    degrees[node1] = degrees.get(node1, 0) + 1
                    degrees[node2] = degrees.get(node2, 0) + 1
    return degrees

def degree_distribution(degrees):
    max_degree = max(degrees.values())
    distribution = [0] * (max_degree + 1)
    for degree in degrees.values():
        distribution[degree] += 1
    return distribution

def plot_degree_distribution(distribution):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(distribution)), distribution, color='b')
    plt.title('Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes')
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.show()

def plot_degree_pdf(distribution):
    total_nodes = sum(distribution)
    pdf = [x / total_nodes for x in distribution]
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(pdf)), pdf, color='r')
    plt.title('Degree PDF')
    plt.xlabel('Degree')
    plt.ylabel('Probability')
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.show()

def plot_degree_cdf(distribution):
    cdf = np.cumsum(distribution) / sum(distribution)
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(cdf)), cdf, marker='o', linestyle='-')
    plt.title('Degree CDF')
    plt.xlabel('Degree')
    plt.ylabel('CDF')
    plt.grid(True)
    plt.show()

# Filepath to your edge list file
filename = 'email-Enron.txt'

# Process the edge list
degrees = read_edge_list(filename)
distribution = degree_distribution(degrees)

# Plotting the results
plot_degree_distribution(distribution)
plot_degree_pdf(distribution)
plot_degree_cdf(distribution)
