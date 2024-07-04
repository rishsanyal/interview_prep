from pprint import pprint

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        ## Sort

        # coins = sorted(coins)

        # coins_matrix = [[10000 for _ in range(0, amount+1)] ]*len(coins)
        # coins_matrix = [[10000 for _ in range(amount + 1)] for _ in range(len(coins))]

        # for i in range(0, len(coins)):
        #     coins_matrix[i][0] = 0

        # for j in range(0, len(coins)):
        #     for k in range(1, amount+1):
        #         coins_matrix[j][k] = min(
        #             coins_matrix[j-1][k],
        #             1 + coins_matrix[j][k - coins[j]]
        #         )
        # #     break


        # return(coins_matrix)

        # return coins_matrix[len(coins)-1][amount]

        dp = [(amount + 1) for _ in range(amount+1)]
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[-1] if dp[-1] != amount + 1 else -1


s = Solution()
pprint(s.coinChange([1, 2, 3], 8))