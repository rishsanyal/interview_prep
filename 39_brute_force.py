class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def helper(currSum, currCandidates, target):

            print(currCandidates)

            if sum(currSum) > target or not currCandidates:
                return False

            if sum(currSum) == target:
                return True

            if currSum in result:
                return False

            nextCandidatesR = [i for i in currCandidates if i <= target]
            nextCandidatesL = nextCandidatesR.copy()

            while nextCandidatesL:
                if helper(currSum + [nextCandidatesL[0]], nextCandidatesL, target):
                    if currSum + [nextCandidatesL[0]] not in result:
                        result.append(currSum + [nextCandidatesL[0]])

                nextCandidatesL.pop(0)

            while nextCandidatesR:
                if helper(currSum + [nextCandidatesR[0]], nextCandidatesR, target):
                    if currSum + [nextCandidatesR[0]] not in result:
                        result.append(currSum + [nextCandidatesR[0]])

                nextCandidatesR.pop(-1)

            return False


        helper([], candidates, target)

        return (result)



s = Solution()
# print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([18,34,2,16,25,6,35], 40))





