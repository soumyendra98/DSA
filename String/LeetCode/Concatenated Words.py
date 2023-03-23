# 472, String + DFS | O((M ^ 3) * N) and O(M * N)
from typing import List


def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    words = set(words)

    def dfs(word, splits):
        for i in range(len(word)):
            if word[:i + 1] in words:
                if i == len(word) - 1:
                    return splits
                else:
                    val = dfs(word[i + 1:], splits + 1)
                    if val: return val
        return 0

    output = []

    for word in words:
        if dfs(word, 0) > 0:
            output.append(word)

    return output
