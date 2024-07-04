class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 == str2:
            return str1

        if len(str1) == len(str2) and str1 != str2 :
            return ""

        smin, smax = min(str1, str2), max(str1, str2)

        for i in range(1, len(smin)+1):
            if len(smin) % i == 0 and len(smax) % i == 0:
                if (smin[:i] * int(len(smin) / i)) == smin and (smin[:i] * int(len(smax) / i)) == smax:
                    return smin[:i]


        return ""






s = Solution()
print(s.gcdOfStrings("ABC", "ABCABC"))