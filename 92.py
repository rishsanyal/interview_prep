# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         seenSet = sorted(set(nums))
#         # nums = list(seenSet) + list([None] * (len(nums) - len(seenSet)))

#         nums = [0]

#         return len(seenSet)

# def removeDuplicates(nums: list[int]) -> int:
#     seenSet = sorted(set(nums))
#     lenNums = len(nums)

#     nums.clear()

#     # tempNums = ["None"]*lenNums
#     # nums[:] = tempNums

#     nums[:] = list(seenSet) + list([None] * (lenNums - len(seenSet)))


#     return len(seenSet)

def removeDuplicates(nums: list[int]) -> int:
    # for i in range(0, len(nums) - 1):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1

    return i


# inputNums = [1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,4]
inputNums = [1,1,2]
print(removeDuplicates(inputNums))
print(inputNums)

