class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        neighbors = defaultdict(list)
        visited = set()
        # reverse_destinations = set()
        edges={(a,b) for a,b  in connections}

        zero_set = set()

        changes = 0

        for src, dst in connections:
            neighbors[src].append(dst)
            neighbors[dst].append(src)

        def dfs(curr_node):
            nonlocal changes
            for i in neighbors[curr_node]:
                if i not in visited:
                    if (i, curr_node) not in edges:
                        changes += 1
                    visited.add(i)
                    dfs(i)

            return

        visited.add(0)
        dfs(0)

        return changes


# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:

#         edges={(a,b) for a,b  in connections}
#         neighbors={city:[] for city in   range(n)}
#         visit=set()
#         changes=0

#         for a,b in connections:
#             neighbors[a].append(b)
#             neighbors[b].append(a)

#         def  dfs(city):
#             nonlocal edges,neighbors,visit,changes

#             for neighbor in neighbors[city]:
#                 if neighbor in visit:
#                     continue

#                 if (neighbor,city) not in edges:
#                     changes +=1

#                 visit.add(neighbor)
#                 dfs(neighbor)

#         visit.add(0)
#         dfs(0)

#         return changes

s = Solution()
print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))