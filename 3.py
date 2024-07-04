class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charactersSeen = {}

        l, r = 0, 0
        resultLen = 0

        while r < len(s):
            if s[r] not in charactersSeen:
                charactersSeen[s[r]] = r

            else:
                ## Reset L to +1 index of it's previous index
                if charactersSeen[s[r]] + 1 > l:
                    l = charactersSeen[s[r]] + 1

                charactersSeen[s[r]] = r

            r += 1

            print(charactersSeen)

            if (r - l) > resultLen:
                resultLen = r - l

        return resultLen


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("pwpwkew")) #4
    # print(s.lengthOfLongestSubstring("dvdf")) #3
    # print(s.lengthOfLongestSubstring("dddf")) #2

    # print(s.lengthOfLongestSubstring("dv")) #2

    print(s.lengthOfLongestSubstring("abba"))


