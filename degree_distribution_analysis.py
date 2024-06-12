import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import powerlaw

# Load the node connections data from the file
node_connections_path = 'erdos_edges.txt'  # Replace with your file path
node_connections = pd.read_csv(node_connections_path, header=None, sep="\t", names=['Node', 'Connected_to'])

# Calculate the degree of each node
node_degrees = node_connections.groupby('Node').size()
print(node_degrees)
# Get frequency of each degree to plot scatter
degree_counts = node_degrees.value_counts().sort_index()
print(degree_counts)
degrees = degree_counts.index
frequencies = degree_counts.values

# Plotting the degree distribution as scatter
plt.figure(figsize=(10, 6))
plt.scatter(degrees, frequencies, color='blue', alpha=0.7)
plt.title('Log-Log Scatter Plot of Degree Distribution with Reference Line')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')

# Adding a reference line with slope -1 for comparison
max_x = max(degrees)
max_y = max(frequencies)
plt.plot([1, max_x], [max_y, max_y / max_x], 'r--', label='Reference line (slope = -1)')
plt.legend()

plt.show()

# Fit the degree distribution to a power-law distribution
data = node_degrees[node_degrees > 0]  # powerlaw package requires positive data
fit = powerlaw.Fit(data)
print('Power-law exponent (alpha):', fit.power_law.alpha)
print('xmin for power law count:', fit.power_law.xmin)

# Compare to a Poisson distribution
R, p = fit.distribution_compare('power_law', 'exponential', normalized_ratio=True)
print('Loglikelihood ratio between power law and exponential:', R)
print('p-value:', p)

# Plotting the fit alongside the actual data for comparison
fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='r', linestyle='--', ax=fig2)
plt.show()
