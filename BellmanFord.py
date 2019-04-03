# Chris Delaney
# Bellman-Ford, Distance-Vector Routing
# Homework 6

import math

graph_edges = [[0, 1, 1],
               [0, 3, 2],
               [1, 0, 1],
               [1, 2, 3],
               [1, 4, 6],
               [2, 1, 3],
               [2, 3, 3],
               [2, 4, 2],
               [3, 0, 2],
               [3, 3, 3],
               [4, 1, 6],
               [4, 2, 2]]

def printPath(P, j):
    if P[j] == -1:
        if j < 2:
            print(chr(j+117), end="")
        else:
            print(chr(j+118), end="")
        return
    printPath(P, P[j])
    if j < 2:
        print(" ->",chr(j+117), end="")
    else:
        print(" ->",chr(j+118), end="")
        

def BellmanFord(graph, src, num_nodes):
    D = [math.inf] * num_nodes
    D[src] = 0
    P = [-1] * num_nodes

    for i in range(num_nodes - 1):
        for node, dest, cost in graph:
            if D[node] != math.inf and D[node] + cost < D[dest]:
                D[dest] = D[node] + cost
                P[dest] = node


    return (D, P)

if __name__ == "__main__":
    D, path = BellmanFord(graph_edges, 4, 5)

    for i in range(5):

        if i < 2:
            print("node: %s \t dist from src: %f" % (chr(i+117), D[i]))
        else:
            print("node: %s \t dist from src: %f" % (chr(i+118), D[i]))

    print("\nForwarding Table")
    print("node\t\tpath")
    print("------------------------------")
    for j in range(5):
        if j < 2:
            print("%s\t|  " % (chr(j+117)), end="")
        else:
            print("%s\t|  " % (chr(j+117)), end="")
        printPath(path, j)
        print()


