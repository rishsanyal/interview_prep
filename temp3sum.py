class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums or len(nums) == 0:
            return []

        if len(nums) < 3:
            return []

        if len(nums) == 3:
            if (nums[0] + nums[1] + nums[2] == 0):
                return [nums]
            else :
                return []

        resList = []

        # tempNums = nums
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            ## Because we've already considered it
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                print(nums[i], nums[l], nums[r])
                currSum = nums[i] + nums[l] + nums[r]

                if currSum == 0:

                    resList.append([nums[i], nums[l], nums[r]])

                    l += 1

                    while l < len(nums) - 1 and nums[l] == nums[l-1]:
                        l += 1

                if currSum > 0:
                    r -= 1

                if currSum < 0:
                    l += 1


        # print(resList)

        return resList


temp = Solution()

# print(temp.threeSum([-1,-3,-4, 4, 0, 1]))
print(temp.threeSum([-1,0,1,0]))