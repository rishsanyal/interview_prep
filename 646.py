class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
           This solution doens't scale for memory usage
        """

        if len(nums) == 1:
            return

        if k == 0:
            return

        def _rotate(nums, k):
            resList = nums * k * 2 # This is the space killer
            slidingWindowEnd = len(resList)
            slidingWindowStart = len(resList) - len(nums)


            for i in range(k, 0, -1):
                print(slidingWindowStart, slidingWindowEnd)
                slidingWindowStart -= 1
                slidingWindowEnd -= 1
            nums[:] = resList[slidingWindowStart:slidingWindowEnd]

        # i = k
        _rotate(nums, k)
        # while i > 1:
        #     _rotate(nums, i)
        #     i -= 1


        def pythonicSolution(nums, k):
            k = k % len(nums)
            nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


# inputNums = [1,2,3,4,5,6,7]
# inputK = 3

inputNums = [1,2]
inputK = 1

sol = Solution()
sol.rotate(inputNums, inputK)

print(inputNums)


# resList = []

# def prints(a, n, ind):
#     i = ind

#     # print from ind-th index to (n+i)th index.
#     while i < n + ind :
#         resList.append(a[i % n])
#         i = i + 1

# # Driver Code
# a = [-1,-100,3,99]
# n = len(a);
# prints(a, n, 2);

# print(resList)