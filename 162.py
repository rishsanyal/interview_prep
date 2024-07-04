class Solution:
    def findPeakElement(self, nums):

        if not len(nums):
            return -1
        if len(nums) == 1:
            return 0

        def bs(low, high):
            ## returns peak

            peak = -1

            # print(low, high)
            mid_num = (low + high) // 2

            if mid_num == 0:
                if nums[mid_num + 1] < nums[mid_num]:
                    return mid_num
                else:
                    return mid_num + 1
            elif mid_num == len(nums) - 1:
                if nums[mid_num - 1] < nums[mid_num]:
                    return mid_num
            else:
                if nums[mid_num - 1] < nums[mid_num] > nums[mid_num + 1]:
                    return mid_num
                else:
                    if nums[mid_num - 1] > nums[mid_num]:
                        return bs(low, mid_num)
                    elif nums[mid_num + 1] > nums[mid_num]:
                        return bs(mid_num, high)
                    else:
                        print('Not this case')
                        return -1


        return bs(0, len(nums) - 1)

s = Solution()

# inp = [1,2,3,1]
inp = [-1, -1, -1]

print(s.findPeakElement(inp))