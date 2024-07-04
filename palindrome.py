class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = s.lower()
        temp = temp.replace(" ", "")
        temp = temp.replace(",", "")
        temp = temp.replace(":", "")
        print(temp)
        evenOrOdd = len(temp) // 2
        stack = []
        midLen = len(temp) // 2



        for i in range(0, len(temp) // 2 + 1):
            stack.insert(0, temp[i])

        if evenOrOdd == 1:
            print(evenOrOdd)
            specialChar = stack.pop()
            midLen = len(temp) // 2

        # for j in range((len(temp) - 1), midLen - 1, -1):
        #     print(temp[j] + ":" + stack.pop())

        for j in range((len(temp) - 1), midLen - 1, -1):
            currChar = stack.pop()
            if temp[j] != currChar:
                return False

        return True


sol = Solution()
print(sol.isPalindrome("racaa=ceacar"))