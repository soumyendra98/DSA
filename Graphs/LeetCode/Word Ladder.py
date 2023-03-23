# 127, BFS | O((M ^ 2) * N) and O((M ^ 2) * N)
from collections import deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    n = len(beginWord)
    wordList = set(wordList)

    if endWord not in wordList:
        return 0

    queue = deque([beginWord])
    visited = {beginWord}
    words = 0

    while queue:
        words += 1
        for _ in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return words

            for i, c in enumerate(word):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if j != c:
                        new_word = word[:i] + j + word[i + 1:]
                        if new_word not in visited and new_word in wordList:
                            queue.append(new_word)
                            visited.add(new_word)
    return 0
