class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        from collections import defaultdict

        ## Get length of each character in the string
        ## It's either the sum of all the even numbers
        ## or it's the sum of all the even numbers + longest odd number

        character_lengths = defaultdict(lambda: 0)
        longest_odd_character_length = 0
        longest_odd_character = ''

        for i in s:
            character_lengths[i] = character_lengths[i] + 1

        for i, j in character_lengths.items():
            if j % 2 != 0 and j > longest_odd_character_length:
                longest_odd_character_length = j
                longest_odd_character = i

        # print(character_lengths)
        # print(longest_odd_character_length)
        result = 0

        for i,j in character_lengths.items():
            if (j % 2 == 0):
                result += j
            else:
                if j >= 1:
                    if longest_odd_character != i:
                        result += j - (j % 2)
                    else:
                        result += longest_odd_character_length

        return result




if __name__ == '__main__':
    s = Solution()

    #

    print(s.longestPalindrome("abccccdd")) # 7