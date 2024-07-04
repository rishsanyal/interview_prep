# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:

#         lastDigit = digits[-1]
#         addedLastDigit = lastDigit + 1
#         carry = False

#         if addedLastDigit == 10:
#             carry = True

#             for i in range(len(digits) - 1, -1, -1):
#                 currDigit = digits[i]

#                 if carry:
#                     if currDigit == 9:
#                         carry = True
#                         digits[i] = 0
#                     else:
#                         digits[i] = digits[i] + 1
#                         carry = False

#                 if (i == 0 and carry):
#                     digits.insert(0, digits[0] + 1)
#                     break

#         else:
#             digits[-1] = digits[-1] + 1


#         return digits

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1 #index to start from the end
        length = len(digits)

        def Calculate(arr, i, length):
            if length > 0 and arr[i] != 9:
                arr[i] += 1
            elif length > 0 and arr[i] == 9:
                arr[i] = 0
                length -= 1
                i -= 1
                Calculate(arr, i, length)
            else: # length == 0 or length < 0
                arr.insert(0, 1)

        Calculate(digits, i, length)
        return digits

sol = Solution()
print(sol.plusOne([9]))
print(sol.plusOne([1,9]))
print(sol.plusOne([1,9,9]))
print(sol.plusOne([1,8,9]))
print(sol.plusOne([9,9]))
print(sol.plusOne([1,2]))