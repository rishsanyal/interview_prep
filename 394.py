class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        # nums_stack = []

        for char in s:
            if char == "]":
                rec_str = ""
                rec_str_num = ""

                while stack[-1] != "[":
                    rec_str = stack.pop() + rec_str

                stack.pop()

                while stack and stack[-1].isdigit():
                    rec_str_num = stack.pop() + rec_str_num

                stack.append(rec_str * int(rec_str_num))
            else:
                stack.append(char)

        return("".join(stack))


# s = "3[a]2[b]"
# s = "3[a2[c]]"
# s = "3[a]2[bc]"
# s = "100[leetcode]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
res_s = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

sol = Solution()
print(sol.decodeString(s))
print(res_s)