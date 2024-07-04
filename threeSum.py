class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        tempNums = nums
        result = []
        tempNums.sort()

        if len(nums) < 3:
            return [nums]

        if len(nums) == 3:
            if (tempNums[0] + tempNums[1] + tempNums[2]) == 0:
                return [tempNums]
            else:
                return []


        for i in range(len(tempNums)):

            if i > 0 and tempNums[i] == tempNums[i - 1]:
                continue

            l, r =  i+1, len(tempNums) - 1

            while l < r:
                currSum = tempNums[l] + tempNums[i] + tempNums[r]

                if currSum == 0:
                    result.append(
                        [tempNums[i], tempNums[l], tempNums[r]]
                    )
                    l = l + 1
                    while l < r and (nums[l] == nums[l-1]):
                        l += 1
                elif currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1

        return result

temp = Solution()

# print(temp.threeSum([-1,-3,-4, 4, 0, 1]))
print(temp.threeSum([-1,0,1,2,-1,-4]))