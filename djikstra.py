# Q=vertices
# [dist[v] = inf for v in vertices]
# [prev[v] = null for v in vertices]
# dist[source] = 0
# while Q is not empty:
# n = Q.pop()
# foreach neighbor i of n:
# if dist[n] + len(n,i) < dist[i] :
# dist[i] = dist[n] + len(n,i)
# prev[i] = n
# return dist, prev

import sys

def dijkstra(graph, source):
    dist = {}
    prev = {}
    Q = []

    for v in graph.keys():
        dist[v] = sys.maxsize
        prev[v] = None
        Q.append(v)

    dist[source] = 0

    while len(Q) > 0:
        n = Q.pop(0)
        for i in graph[n].keys():
            if dist[n] + graph[n][i] < dist[i]:
                dist[i] = dist[n] + graph[n][i]
                prev[i] = n

    return dist, prev

def main():
    # Using adjacency list
    graph = {
        'a': {'b': 7, 'c': 9, 'f': 14},
        'b': {'a': 7, 'c': 10, 'd': 15},
        'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
        'd': {'b': 15, 'c': 11, 'e': 6},
        'e': {'d': 2, 'f': 9},
        'f': {'a': 14, 'c': 2, 'e': 9}
    }

    dist, prev = dijkstra(graph, 'e')

    print(dist)
    print(prev)

if __name__ == '__main__':
    main()