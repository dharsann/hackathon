import json
import networkx as nx

# Load the JSON data from the file
with open(r'Z:\Hackathon\Input data\level0.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the distances for neighborhoods and the restaurant
neighborhood_distances = {key: value['distances'] for key, value in data['neighbourhoods'].items()}
restaurant_distances = data['restaurants']['r0']['neighbourhood_distance']

# Add the restaurant distances to the neighborhood distances
neighborhood_distances['r0'] = restaurant_distances

# Convert the distances into an adjacency matrix
num_neighborhoods = len(neighborhood_distances)
adjacency_matrix = [neighborhood_distances[key] for key in sorted(neighborhood_distances.keys())]

# Create a graph from the adjacency matrix
G = nx.Graph()
for i in range(num_neighborhoods + 1):  # Include the restaurant node
    for j in range(num_neighborhoods + 1):  # Include the restaurant node
        G.add_edge(i, j, weight=adjacency_matrix[i][j])

# Perform any further operations using the created graph `G`
# For example, find the shortest path:
shortest_path = nx.approximation.traveling_salesman_problem(G, cycle=True)

# Print the shortest path
print(shortest_path)


G = nx.Graph()
num_nodes = len(adjacency_matrix)
for i in range(num_nodes):
    for j in range(num_nodes):
        G.add_edge(i, j, weight=adjacency_matrix[i][j])

tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)
restaurant_index = num_nodes - 1
while tsp_path[0] != restaurant_index:
    tsp_path = tsp_path[1:] + tsp_path[:1]
node_names = ['n{}'.format(i) for i in tsp_path]
node_names = ['r0'] + node_names + ['r0']
output = {"v0": {"path": node_names}}

