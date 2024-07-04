def maxVacationDays(flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        mydict = {}

        for i in range (len(flights)):
            if i not in mydict:
                mydict[i] = [i]
            for j in range (len(flights)):
                if flights[i][j] == 1:
                    mydict[i].append(j)

        dp = [[0]*len(days[0]) for _ in range (len(days))]
        for i in range (len(dp)):
            dp[i][-1] = days[i][-1]


        for k in range (len(dp[0])-2,-1,-1):
            for i in range (len(dp)):
                for a in mydict[i]:
                    dp[i][k] = max(dp[i][k], dp[a][k+1]+days[i][k])


        res = 0
        for val in mydict[0]:
            res = max(res,dp[val][0])


        print(dp)

        return res


# flights = [[0,1,1],[1,0,1],[1,1,0]]
# days = [[1,3,1],[6,0,3],[3,3,3]]

# flights = [[0,0,0],[0,0,0],[0,0,0]]
# days = [[1,1,1],[7,7,7],[7,7,7]]

flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[7,0,0],[0,7,0],[0,0,7]]

print(maxVacationDays(flights,days))