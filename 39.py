class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(list(cur))
                return

            if i >= len(candidates) or total > target:
                return

            # Choose to include candidates at i
            cur.append(candidates[i])
            dfs(i, cur, sum(cur))
            cur.pop()

            dfs(i + 1, cur, sum(cur))

        dfs(0, [], 0)

        return res

s = Solution()
# print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([18,34,2,16,25,6,35], 40))





