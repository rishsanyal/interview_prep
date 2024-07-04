class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from collections import defaultdict

        value_dict = defaultdict(int)

        maxNum = -1

        for i in nums:
            value_dict[i] += i
            maxNum = max(i, maxNum)

        cache = [0 for _ in range(maxNum+1)]

        cache[0] = value_dict[0]
        cache[1] = value_dict[1]

        for i in range(2, maxNum+1):
            cache[i] = max(cache[i-2] + value_dict[i], cache[i-1])

        return max(cache[maxNum], cache[maxNum-1])


if __name__ == '__main__':

    nums = [2,2,3,3,3,4]

    s = Solution()
    print(s.deleteAndEarn(nums))