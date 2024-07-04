class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        reference_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        # half_len = len(s) // 2

        closing_parantheses_stack = []

        for i in range(0, len(s)):
            if s[i] in reference_map:
                closing_parantheses_stack.append(reference_map[s[i]])
            else:
                if len(closing_parantheses_stack) == 0 or s[i] != closing_parantheses_stack.pop():
                    return False

        # return

        # for i in range(0, half_len):
        #     if s[i] not in reference_map:
        #         print(s[i])
        #         return False
        #     else:
        #         closing_parantheses_stack.append(reference_map[s[i]])


        # for i in range(half_len, len(s)):
        #     if closing_parantheses_stack.pop() != s[i]:
        #         return False

        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.isValid('()'))
    print(s.isValid("()[]{}"))