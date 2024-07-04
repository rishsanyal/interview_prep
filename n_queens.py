# class Solution:

#     def solveNQueens(self, n: int) -> List[List[str]]:

#         col= set()
#         posDiag = set()
#         negDiag =  set()

#         res = []
#         board = [['.'] * n for i in range(n)]

#         def backTrack(r):
#             if r==n:
#                 copy =  ["".join(row) for row in board]
#                 res.append(copy)
#                 return

#             for c in range(n):
#                 if c in col or (r+c) in posDiag or (r-c) in negDiag:
#                     continue

#                 col.add(c)
#                 posDiag.add(r+c)
#                 negDiag.add(r-c)
#                 board[r][c] = "Q"

#                 backTrack(r+1)

#                 col.remove(c)
#                 posDiag.remove(r+c)
#                 negDiag.remove(r-c)
#                 board[r][c] = "."

#         backTrack(0)
#         return res





class Solution:
    def solveNQueens(self, n: int):

        diagonal_set = set()
        graph = []


        def __findPath(queen_set, curr_col=0):
            ## We recurse here per column
            ans = []

            if curr_col == n or len(queen_set) == n:
                graph.append(list(queen_set))
                # queen_set.clear()
                return

            if len(queen_set) == 0:
                for i in range(0, n):
                    temp_set = set()
                    temp_set.add((i, 0))

                    __findPath(temp_set, curr_col+1)

                    temp_set.remove((i, 0))

                    # if res:
                    #     graph.append(res)

            else:
                match_found = False
                for i in range(0, n):
                    if __validateLocation(queen_set, (i, curr_col)):
                        queen_set.add((i, curr_col))

                        __findPath(queen_set, curr_col+1)
                        match_found = True

                        queen_set.remove((i, curr_col))

                        # if res:
                        #     ans.append(res)

                if not match_found:
                    __findPath(queen_set, curr_col+1)
                    match_found = True
                    # if res:
                    #     ans.append(res)

            return ans

        def __validateLocation(queen_set, new_queen_locn):
            # Rules:
            # Can't be in the same row/col
            # Can't be present diagonally

            """Returns true if valid location"""

            new_x, new_y = new_queen_locn

            for curr_queen in queen_set:
                curr_x, curr_y = curr_queen

                if curr_x == new_x or curr_y == new_y:
                    return False

            temp_set = queen_set.copy().union(set([new_queen_locn]))

            for diagonal in diagonal_set:
                if len(diagonal.intersection(temp_set)) > 1:
                    return False

            return True

        ## generate diagonal sets
        # check if multiple queens are present in the diagonal

        def __generateDiagonalSet():
            result = []
            temp_set = set()

            ## generate downward diagonals for each row
            for i in range(0, n):
                for j in range(0, 1):
                    curr_x = i
                    curr_y = j

                    while curr_x >= 0 and curr_y >= 0 and curr_x < n and curr_y < n:
                        temp_set.add((curr_x, curr_y))
                        curr_x += 1
                        curr_y += 1

                    result.append(temp_set)
                    temp_set = set()

            ## generate downward diagonals for each row
            for i in range(0, 1):
                for j in range(0, n):
                    curr_x = i
                    curr_y = j

                    while curr_x >= 0 and curr_y >= 0 and curr_x < n and curr_y < n:
                        temp_set.add((curr_x, curr_y))
                        curr_x += 1
                        curr_y += 1

                    result.append(temp_set)
                    temp_set = set()

            ## generate upward diagonals for each row
            for i in range(n-1, -1, -1):
                for j in range(0, 1):
                    curr_x = i
                    curr_y = j

                    while curr_x >= 0 and curr_y >= 0 and curr_x < n and curr_y < n:
                        temp_set.add((curr_x, curr_y))
                        curr_x -= 1
                        curr_y += 1

                    result.append(temp_set)
                    temp_set = set()

            for j in range(0, n):
                curr_x = n-1
                curr_y = j

                while curr_x >= 0 and curr_y >= 0 and curr_x < n and curr_y < n:
                    temp_set.add((curr_x, curr_y))
                    curr_x -= 1
                    curr_y += 1

                result.append(temp_set)
                temp_set = set()

            return result

        def __createGraph():
            temp_graph_list = []

            # print(graph)

            for point_list in graph:
                temp_graph = [['.' for _ in range(n)] for _ in range(n)]
                for point in point_list:
                    x, y = point
                    temp_graph[x][y] = 'Q'

                for i in range(len(temp_graph)):
                    temp_graph[i] = "".join(temp_graph[i])

                temp_graph_list.append(temp_graph)

            return temp_graph_list

        diagonal_set = __generateDiagonalSet()

        for i in diagonal_set:
            print(i)
            print("=====")

        __findPath(set())

        graph = [i for i in graph if len(i) == n]

        graph = __createGraph()

        return graph

s = Solution()
print(s.solveNQueens(5)) # 2