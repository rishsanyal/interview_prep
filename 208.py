class Node(object):
    def __init__(self, letter=None):
        self.letter = letter
        self.next = {}


class Trie(object):
    def __init__(self):
        # self.tracker = set()
        self.starter = Node("#")

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        # self.tracker.add(word)

        curr_char = "#"
        word_len = 0 #, len(word)

        curr_node = self.starter

        while word_len < len(word) and word[word_len] in curr_node.next:
            curr_node = curr_node.next[word[word_len]]
            word_len += 1

        while word_len < len(word):
            curr_node.next[word[word_len]] = Node(word[word_len])
            curr_node = curr_node.next[word[word_len]]
            word_len += 1

        curr_node.next['#'] = Node("#")

        return

    def printAll(self):
        nodes = [self.starter]

        while nodes:
            curr_node = nodes.pop()

            print(curr_node.letter)

            nodes.extend(curr_node.next.values())


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        word_len = 0
        curr_node = self.starter

        while word_len < len(word):
            if word[word_len] not in curr_node.next.keys():
                return False

            curr_node = curr_node.next[word[word_len]]
            word_len += 1

        return ("#" in curr_node.next)


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        word_len = 0
        curr_node = self.starter

        while word_len < len(prefix):
            if prefix[word_len] not in curr_node.next.keys():
                break

            curr_node = curr_node.next[prefix[word_len]]
            word_len += 1

        # print(word_len)
        # print(len(prefix) - 1)

        return word_len == len(prefix)




# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
# obj.insert("terror")
# obj.printAll()
param_2 = obj.search("apple")
print(param_2)

param_2 = obj.search("app")
print(param_2)

param_3 = obj.startsWith("b")
print(param_3)