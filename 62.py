# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """


#         def currSteps(currM, currN, DP):
#             for i in range(0, currM):
#                 DP[i][0] = 1
#             for j in range(0, currN):
#                 DP[0][j] = 1

#             for i in range(1, currM):
#                 for j in range(1, currN):
#                     DP[i][j] = DP[i-1][j] + DP[i][j-1]

#             return DP[currM-1][currN-1]


#         tempPaths = 0
#         tempArr = [[None]*(n+1)]*(m+1)

#         # print(tempArr)

#         return(currSteps(m, n, tempArr))

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        visited_arr = [[0 for _ in range(n)] for _ in range(m)]
        # visited_arr = [[None]*(n+1)]*(m+1) #[[None] * n] * m

        for i in range(m):
            visited_arr[i][n-1] = 1

        ## 0 - 2
        for j in range(n):
            visited_arr[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                visited_arr[i][j] = visited_arr[i+1][j] + visited_arr[i][j+1]

        return visited_arr[0][0]

s = Solution()

print(s.uniquePaths(3,7))