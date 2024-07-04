class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        if not chars:
            return []

        s = ""

        currChar = chars[0]
        currCharStart = 0
        currCharEnd = 1

        count = 0

        delimiter = "$%"

        ## Iterate through the chars
        ## Track starting index
        ## Perform look-ahead for end index
        ## create the resulting array
        ## Get it up to length according to all the characters found with special character #
        ## remove all special characters

        while count < len(chars)-1:
            if chars[count] != chars[count+1]:
                charLen = currCharEnd - currCharStart #2

                temp = ""
                if charLen > 1:
                    for i in str(charLen):
                        temp += i + delimiter

                s += currChar + delimiter + temp  # A2

                ## We need to replace the list with this

                currCharStart = count + 1
                currChar = chars[count+1]

            currCharEnd += 1
            count += 1

        charLen = currCharEnd - currCharStart #2

        if charLen > 1:
            temp = ""
            for i in str(charLen):
                temp += i + delimiter
            tempInpStr = currChar + delimiter + temp  # A2
        else:
            tempInpStr = currChar

        s += tempInpStr

        if len(s) > 1:
            chars[:] = [str(i) for i in s.split(delimiter)]

            if chars[-1] == "":
                chars[:] = chars[:-1]
        else:
            chars[:] = s.split(delimiter)

        print(chars)
        print(s)

        return len(chars)


# class Solution(object):
#     def compress(self, chars):
#         n = len(chars)
#         if n == 1:
#             return 1

#         write_idx = 0
#         curr_idx = 0
#         while curr_idx < n:
#             curr_char = chars[curr_idx]
#             cnt = 0
#             while curr_idx < n and chars[curr_idx] == curr_char:
#                 curr_idx += 1
#                 cnt += 1
#             chars[write_idx] = curr_char
#             write_idx += 1
#             if cnt > 1:
#                 cnt_str = str(cnt)
#                 for i in range(len(cnt_str)):
#                     chars[write_idx] = cnt_str[i]
#                     write_idx += 1

#         return write_idx

# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """

#         if not chars:
#             return []


#         write_index = 0
#         count = 0
#         currPtr = 0

#         delimiter = "$%"

#         ## Iterate through the chars
#         ## Track starting index
#         ## Perform look-ahead for end index
#         ## create the resulting array
#         ## Get it up to length according to all the characters found with special character #
#         ## remove all special characters

#         while currPtr < len(chars):
#             count = 0
#             currChar = chars[currPtr]

#             currCharStart = currPtr
#             currCharEnd = currPtr

#             while currPtr < len(chars) and chars[currPtr] == currChar:
#                 count += 1
#                 currPtr += 1
#                 currCharEnd += 1

#             chars[currCharStart] = currChar
#             write_index += 1

#             if count > 1:
#                 count_str = str(count)

#                 for i in range(len(count_str)):
#                     chars[write_index] = count_str[i]
#                     write_index += 1

#         return write_index


s = Solution()

chars = ["a","a","b","b","b", "c","c","c"]

print(s.compress(chars))

print(chars)