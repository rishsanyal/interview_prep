from typing import List
from collections import defaultdict
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import deque

        wordSet = set(wordList)\

        if endWord not in wordSet:
            return []

        visited = set()
        q = deque([[beginWord]])
        ans = []

        while q:
            curr_res = set()
            for _ in range(len(q)):
                curr_words = q.popleft()
                last_word = curr_words[-1]

                if curr_words[-1] == endWord:
                    ans.append(curr_words)
                else:
                    for i in range(len(last_word)):
                        for c in string.ascii_lowercase:
                            new_word = last_word[:i] + c + last_word[i+1:]
                            if new_word in wordSet and new_word not in visited:
                                q.append(curr_words+[new_word])
                                curr_res.add(new_word)

            visited.update(curr_res)

        return(ans)

# Time complexity: O(N * M) where N is the number of words and M is the length of each word
s = Solution()
print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]