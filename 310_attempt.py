class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # Find the height of the tree, picking every node as the root
        # Height has to range from 0 to n
        # create a dict with the height and the root

        if n == 1:
            return [0]
        if n == 2:
            return [0,1]


        from collections import defaultdict, deque

        ## Make an adjacency list
        adj_dict = defaultdict(set)

        for i, j in edges:
            adj_dict[i].add(j)
            adj_dict[j].add(i)

        ## Add all leaf nodes to a queue
        q = deque()

        for i,j in adj_dict.items():
            if len(j) == 1:
                q.append(i)

        ## while n > 2
        ## currLen = len(q)
        ## n -= currLen
        ## For every node in queue:
        ## for all of it's neighbors
        ## we remove it's adjacency with it's neightbors
        ## if neighbor has one neighbor (it jsut turned into a leaf node) we add it to the queue


        while n>2:
            currLen = len(q)
            n -= currLen

            for _ in range(currLen):
                curr_node = q.popleft()

                for neighbor in adj_dict[curr_node]:
                    # adj_dict[curr_node].remove(neighbor)
                    adj_dict[neighbor].remove(curr_node)

                    if len(adj_dict[neighbor]) == 1:
                        q.append(neighbor)

        return list(q)

# test = (4, [[1,0],[1,2],[1,3]])
test = (6, [[3,0],[3,1],[3,2],[3,4],[5,4]])

s = Solution()

print(s.findMinHeightTrees(test[0], test[1]))