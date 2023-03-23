# 269,
from collections import defaultdict, deque
from typing import List


def alienOrder(words: List[str]) -> str:
    graph = defaultdict(set)
    indegree = defaultdict(int)
    output = []
    chars = set()
    n = len(words)
    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        m = min(len(w1), len(w2))
        for j in range(m):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
            elif j == m - 1 and len(w1) > len(w2):
                return ""

    for word in words:
        for char in word:
            chars.add(char)

    queue = deque([i for i in chars if i not in indegree])
    count = 0

    while queue:
        char = queue.popleft()
        output.append(char)
        for next_char in graph[char]:
            indegree[next_char] -= 1
            if indegree[next_char] == 0:
                queue.append(next_char)
        count += 1
    if count != len(chars):
        return ""
    return "".join(output)
