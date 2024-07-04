class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        def findPivot(nums, inpL, inpR):
            ## Find the smallest number in the array

            l, r = inpL, inpR
            midpoint = (l + r) // 2
            # tempMid = int((l+r)/2)

            # print(midpoint, tempMid)

            # print(l, r)

            if inpR < inpL:
                return -1
            elif inpR == inpL:
                return inpR
            else:

                # if len(nums) == 1:
                #     return 0
                # if len(nums) == 2:
                #     if nums[0] < nums[1]:
                #         return 0
                #     return 1

                if midpoint < r and nums[midpoint] > nums[midpoint+1]:
                    return midpoint
                if midpoint > l and nums[midpoint] < nums[midpoint-1]:
                    return midpoint-1
                if nums[l] >= nums[midpoint] :
                    return findPivot(nums, l, midpoint-1)

                return findPivot(nums, midpoint + 1, r)



        def binarySearch(nums, target):
            ## Find the index of target and return it

            targetIndex = -1
            l, r = 0, len(nums)

            if len(nums) == 0:
                return targetIndex
            elif len(nums) == 1:
                if (nums[0] == target):
                    targetIndex = 0
            elif len(nums) == 2:
                if (nums[0] == target):
                    targetIndex = 0
                if (nums[1] == target):
                    targetIndex = 1
            else:
                midpoint = (l + r -1) // 2

                if target == nums[midpoint]:
                    return midpoint
                else:
                    if target < nums[midpoint]:
                        return binarySearch(nums[l:midpoint], target)
                    else:
                        temp = binarySearch(nums[midpoint:], target)
                        if temp == -1:
                            return -1
                        else:
                            targetIndex = midpoint + temp
            return targetIndex




        pivotIndex = findPivot(nums, 0, len(nums)-1)

        # print(pivotIndex)

        leftList, rightList = nums[0:pivotIndex+1], nums[pivotIndex+1:]

        # print(leftList, rightList)

        leftIndex = binarySearch(leftList, target)
        rightIndex = binarySearch(rightList, target)

        # print(leftIndex, rightIndex, pivotIndex)

        if leftIndex == -1 and rightIndex == -1:
            return -1
        else:
            if rightIndex != -1:
                if leftIndex == -1:
                    return pivotIndex + rightIndex + 1
            return leftIndex

        return -1




s = Solution()
# inpList = [4,5,6,7,0,1,2,3]
# inpList = [4,5,6,7,0,1,2,3]
inpList = [3,4,5,6,1,2]
# print(s.search(inpList, 3))
for i in inpList:
    print(s.search(inpList, i))

# print(s.search(inpList, 3))