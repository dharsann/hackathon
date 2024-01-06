import json
from sys import maxsize
from itertools import permutations


with open(r'Z:\Hackathon\Input data\level0.json','r') as f:
    o=json.load(f)

print(json.dumps(o))

def tsp(graph,s):
    vertex=[]
    for i in range(V):
        if i!=s:
            vertex.append(i)
    min_cost=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_cost=0
        k=s
        for j in i:
            current_cost+=graph[k][j]
            k=j
        current_cost+=graph[k][s]
        min_cost=min(min_cost,current_cost)
    return vertex


