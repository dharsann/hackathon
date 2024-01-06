import json
import numpy as np
with open(r'Z:\Hackathon\Input data\level0.json') as file:
    data = json.load(file)

adj_mat = []
for i in range(data['n_neighbourhoods']):
    row = data['neighbourhoods']['n'+str(i)]['distances']
    adj_mat.append(row)

adj_mat.insert(0, data['restaurants']['r0']['neighbourhood_distance'])

adj_mat[0].insert(0, 0)
for i in range(1, len(adj_mat)):
    adj_mat[i].insert(0, adj_mat[0][i])

def nearest_neighbor(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    
    path = [start]
    visited[start] = True
    current = start
    
    while len(path) < num_nodes:
        nearest_node = None
        min_distance = np.inf
        
        for i in range(num_nodes):
            if not visited[i] and graph[current][i] < min_distance:
                min_distance = graph[current][i]
                nearest_node = i
        
        if nearest_node is not None:
            path.append(nearest_node)
            visited[nearest_node] = True
            current = nearest_node
    
    path.append(start) 
    
    return path

path = nearest_neighbor(adj_mat, 0)

output = {'v0': {'path': []}}
for i in path:
    if i == 0:
        output['v0']['path'].append('r0')
    else:
        output['v0']['path'].append('n'+str(i-1))

data=json.dumps(output)
with open('outfile.json','w') as json_file:
    json_file.write(data)

print(data)