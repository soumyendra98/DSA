# 212, Create Trie for the word list and DFS with all indexes in the matrix | O(M * 4 * (3 ^ (L - 1))) and O(N)
# where N is the total no of Words
# M is the no of cells and
# L is the length of the word
from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:

    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        node = self.root
        for val in word:
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.isEndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie(words)
        output = set()
        visited = set()

        def dfs(r, c, node, word):
            if r < 0 or r == m or c < 0 or c == n or (r, c) in visited or board[r][c] not in node.children:
                return
            temp = board[r][c]
            word += temp
            node = node.children[temp]

            if node.isEndOfWord:
                output.add(word)
                if len(node.children) == 0:
                    del node
                    return

            visited.add((r, c))

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visited.remove((r, c))

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, '')

        return list(output)
