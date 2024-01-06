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
