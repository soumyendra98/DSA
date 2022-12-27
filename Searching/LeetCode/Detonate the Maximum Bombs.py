# 2101, Create A graph using Radius < Distance | O(N ^ 3) and O(N ^ 2)
from collections import defaultdict
from typing import List


def maximumDetonation(bombs: List[List[int]]) -> int:
    graph = defaultdict(list)
    n = len(bombs)
    for i in range(n):
        x1, y1, r1 = bombs[i]
        for j in range(n):
            if i == j:
                continue

            x2, y2, r2, = bombs[j]

            if r1 ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:
                graph[i].append(j)

    def dfs(idx, visited):
        if idx in visited:
            return 0
        visited.add(idx)
        count = 1
        for j in graph[idx]:
            count += dfs(j, visited)
        return count

    max_exp = -1
    for i in range(n):
        max_exp = max(max_exp, dfs(i, set()))
    return max_exp
