# 208, Trie Implementation using HashMap | O(N) and O(N)
class TrieNode:

    def __init__(self):
        self.children = {}

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for val in word:
            if ord(val) - 97 in node.children:
                node = node.children[ord(val) - 97]
            else:
                node.children[ord(val) - 97] = TrieNode()
                node = node.children[ord(val) - 97]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for val in word:
            if ord(val) - 97 not in node.children:
                return False
            else:
                node = node.children[ord(val) - 97]

        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for val in prefix:
            if ord(val) - 97 not in node.children:
                return False
            else:
                node = node.children[ord(val) - 97]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
