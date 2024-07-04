class Solution(object):
    def addBinary(self, a, b):
        import math
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        leftSum = 0
        rightSum = 0

        for i in range(0, len(a)):
            if a[i] == "1":
                leftSum += math.pow(2, len(a) - i - 1)

        for i in range(0, len(b)):
            if b[i] == "1":
                rightSum += math.pow(2, len(b) - i - 1)

        finalSumInt = int(leftSum + rightSum)

        result = ""

        tempSumInt = finalSumInt

        if finalSumInt == 0:
            return "0"

        while tempSumInt > 0:
            result += str(tempSumInt % 2)
            tempSumInt = tempSumInt // 2

        return result[::-1]


if __name__ == '__main__':
    s = Solution()

    # print(s.addBinary("1010", "1100")) # 10110

    print(s.addBinary("0", "0")) # 10111







