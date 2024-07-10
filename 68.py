from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        # Split words into a 2d array
        # Where the total length of each array should be less than maxWidth
        # There should be a space appended after every entry, so it's len(word) + 1 for each entry

        # Come back to spacing between words

        result = []

        temp = []
        len_temp = 0

        words_q = words[:]

        while words_q:
            curr_word = words_q.pop(0)

            if len_temp + len(curr_word) > maxWidth:
                result.append(temp)

                temp = [curr_word]
                len_temp = len(curr_word)+1

            else:
                temp.append(curr_word)

                len_temp += len(curr_word) + 1


        result.append(temp)

        ctr = 0


        for row in result[:-1]:
            res = sum([len(i) for i in row])
            prev_len = len(row)
            num_spaces = maxWidth - res
            pos = 1


            if len(row) - 1 == 0:
                row.insert(pos, " "*num_spaces)
            else:
                curr_spaces = (num_spaces//(prev_len-1)) + (num_spaces % (prev_len-1))

                while num_spaces > 0:
                    row.insert(pos, " " * curr_spaces)

                    pos += 2

                    num_spaces -= curr_spaces

        # For the last line
        # print()
        last_space = (maxWidth - sum([len(i) for i in result[-1]]))
        pos = 1
        if len(result[-1]) > 1:
            for i in range(len(result[-1][:-1])):
                result[-1].insert(pos, " ")
                last_space -= 1

        result[-1].append(" " * last_space)



        # result[-1].append(last_space)


        for i in range(len(result)):
            result[i] = "".join(result[i])


        return result





s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))