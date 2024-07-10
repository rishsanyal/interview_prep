
## Q1: Check if every service can call every other service
## BFS for each of them to find all services they can talk to
## Once we have the adjacency map,
## we check the number of services vs the total number of services

## If we hit A first, we know A can talk to all services -> If any other service hits A, it can talk to all services
## We can pop off all of the services that A talks to
## We have a remainder that doesn't talk to A but talks to other services that talk to A, then it also can talk to all services
## We can filter accordingly

from collections import defaultdict
from queue import deque

def isConnected(inp_list):

    if not inp_list:
        return False

    initial_connections = defaultdict(set)

    for origin, dest in inp_list:
        initial_connections[origin].add(dest)
        initial_connections[dest].add(origin)

    is_completely_connected = set()

    for service in initial_connections.keys():
        q = deque([service])
        visited = set([service])

        while q:
            curr_service = q.popleft()

            for connection in initial_connections[curr_service]:
                if curr_service in is_completely_connected or connection in is_completely_connected:
                    is_completely_connected.update(set(initial_connections[curr_service]))
                    is_completely_connected.update(visited)
                    continue

                if connection not in visited:
                    q.append(connection)
                    visited.add(connection)

                    if len(visited) == len(initial_connections.keys()):
                        is_completely_connected.add(connection)
                        is_completely_connected.update(visited)


    if len(is_completely_connected) == len(initial_connections.keys()):
        return True

    return False

# We have the adj graph
# we go to bfs
# If we hit a previously visited node, we know that rule is redundant
# we pop it from the rules set

#

def findConnected(inp_list):

    if not inp_list:
        return False

    initial_connections = defaultdict(set)

    rules = set()

    for origin, dest in inp_list:
        initial_connections[origin].add(dest)
        initial_connections[dest].add(origin)

        rules.add((origin, dest))
        # rules.add((dest, origin))

    for service in initial_connections.keys():
        q = deque([service])
        visited = set([service])
        original_service = service

        while q:
            curr_service = q.popleft()

            for connection in initial_connections[curr_service]:

                if connection == original_service:
                    if (connection, curr_service) in rules:
                        rules.remove((connection, curr_service))

                if connection not in visited:
                    q.append(connection)
                    visited.add(connection)

    print(rules)

    return False

print(findConnected([
    ["A", "B"],
    ["C", "A"],
    ["C", "B"]
]))
"""
[
    a: b,
    c: b,
    b: c
]

[
    a: b, c
    b: a, c
    c: b, a
]
"""



# Sample Case 1
# Input:



# [
#     ["BoxSign", "Monolith"],
#     ["Conversion", "BoxSign"],
#     ["Conversion", "Monolith"]
# ]




# Potential output:

# [
#   ["BoxSign", "Monolith"],
#   ["Conversion", "Monolith"]
# ]
# Since all nodes are connected in a cycle in the input, so removing any pair would be ok.





# Sample Case 2
# Input



# [
#      ["BoxSign", "Monolith"],
#      ["BoxSign", "Conversion"],
#      ["BoxSign", "Preview"],
#      ["Monolith", "Conversion"],
#      ["Conversion", "Preview"],
#      ["Conversion", "Search"],
# ]




# Potential output:

# [
#   ["BoxSign", "Monolith"],
#   ["BoxSign", "Conversion"],
#   ["Conversion", "Preview"],
#   ["Conversion", "Search"]
# ]