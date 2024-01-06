import json

with open(r'Z:\Hackathon\Input data\level0.json', 'r') as f:
    graph = json.load(f)

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph['neighbourhoods']}
    distances[start] = 0
    visited_nodes = set()
    previous_nodes = {}

    while len(visited_nodes) < len(graph['neighbourhoods']):
        min_distance = float('inf')
        min_node = None
        for node in graph['neighbourhoods']:
            if node not in visited_nodes and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        visited_nodes.add(min_node)

        for idx, distance in enumerate(graph['neighbourhoods'][min_node]['distances']):
            neighbour = 'n' + str(idx)
            if neighbour not in visited_nodes and distance != "INF":
                new_distance = distances[min_node] + distance
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    previous_nodes[neighbour] = min_node

    path = [end]
    current_node = end
    while current_node != start:
        current_node = previous_nodes[current_node]
        path.append(current_node)
    path.reverse()
    path.insert(0, start)

    return path

def find_shortest_path(graph, restaurant, start, end):
    shortest_path = dijkstra(graph, start, end)
    return shortest_path

restaurant = 'r0'  
start_node = 'n0'
end_node = 'n9'

shortest_path = find_shortest_path(graph, restaurant, start_node, end_node)

output = {"v0": {"path": ['r0']+shortest_path+['r0']}}

with open(r"Z:\Hackathon\level0out.json", 'w') as outfile:
    json.dump(output, outfile)

print(json.dumps(output))
