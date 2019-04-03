#Chris Delaney
#Homework 5
#Dijkstra's Algorithm

import math

graph = [[0, 2, 5, 1, 0, 0],
         [2, 0, 3, 2, 0, 0],
         [5, 3, 0, 3, 1, 5],
         [1, 2, 3, 0, 1, 0],
         [0, 0, 1, 1, 0, 2],
         [0, 0, 5, 0, 2, 0]]

def printPath(P, j):
    if P[j] == -1:
        print(j, end="")
        return
    printPath(P, P[j])
    print(" ->",j, end="")

def minD(D, num_v, inN):
    minimum = math.inf
    min_i = -1
    for v in range(0, num_v):
        if D[v] < minimum and v not in inN:
            minimum = D[v]
            min_i = v 
    
    return min_i

def dijkstra(graph, src):
    N = []
    D = [math.inf] * len(graph)
    path = [-1] * len(graph)
    inN = [-1] * len(graph)
    inN[src] = src
    N.append(src)
    
    for v in range(0, len(graph)):
        if graph[src][v] != 0:
            D[v] = graph[src][v]
        else:
            D[v] = math.inf
    D[src] = 0

    for i in range(0, len(graph)):
        w = minD(D, len(graph), inN)
        N.append(w)
        inN[w] = w

        for v in range(0, len(graph)):
            if graph[w][v] > 0 and v not in N and D[v] > D[w] + graph[w][v]:
                D[v] = D[w] + graph[w][v]
                path[v] = w
    
    return (N, D, path)

src = 5
distance = dijkstra(graph, src)
D = distance[1]
N = distance[0]
path = distance[2]

print("src = Node ", src, " (Node Z)")

for j in range(0, len(graph)):
    print("node: %d\t dist from source: %d\t" % (j, D[j]))

print()
print("destination\t | \tlink")
print("-" * 30)
for k in range(0, len(graph)):
    print(k, "\t\t |  ", end="")
    printPath(path, k)
    print()


