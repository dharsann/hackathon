import json
import networkx as nx

with open(r'Z:\Hackathon\Input data\level0.json', 'r') as json_file:
    data = json.load(json_file)

neighborhood_distances = {key: value['distances'] for key, value in data['neighbourhoods'].items()}
restaurant_distances = data['restaurants']['r0']['neighbourhood_distance']
neighborhood_distances['r0'] = restaurant_distances
num_neighborhoods = len(neighborhood_distances)
adjacency_matrix = []
for key in sorted(neighborhood_distances.keys()):
    adjacency_matrix.append(neighborhood_distances[key])

G = nx.Graph()
G.add_nodes_from(range(num_neighborhoods + 1))
for i in range(num_neighborhoods + 1):  
    for j in range(num_neighborhoods + 1):  
        G.add_edge(i, j, weight=adjacency_matrix[i][j])
tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)
node_names = ['n{}'.format(node_index) for node_index in tsp_path]
node_names = ['r0'] + node_names + ['r0']
output = {"v0": {"path": node_names}}

print(output)
