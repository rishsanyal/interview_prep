class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l, curr_sum = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                res = min(r - l + 1, res)
                curr_sum -= nums[l]
                l += 1

        return 0 if res == float('inf') else res


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(
        11,
        [1,2,3,4,5]
    ))