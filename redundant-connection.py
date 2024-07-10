class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # variable to keep track of graph constructed so far
        graph_so_far = defaultdict(list)

        # dfs function to check if path exists between nodes u and v
        def path_exists(u, v, visited):
            # we reached to v from u
            if u == v:
                return True

            # mark u as visited
            visited.add(u)

            # iterate through all the neighbors of u and if they are not visited call dfs on them
            for neighbor in graph_so_far[u]:
                if neighbor not in visited:
                    if path_exists(neighbor, v, visited):
                        return True

            return False

        # iterate through all the pairs of edges
        for u, v in edges:
            # we make a fresh visited because we call dfs for every pair of edges
            # if path exists between u and v return that's the answer
            if path_exists(u,v,set()):
                return [u,v]
            else:
                # if path does not exist we add edges to graph
                graph_so_far[u].append(v)
                graph_so_far[v].append(u)

        return None


s = Solution()

