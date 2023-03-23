# 1615, Degree of Graph | O(N ^ 2) and O(N ^ 2)
from typing import List


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    graph = [[] for _ in range(n)]

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    max_val = 0

    for i in range(n):
        for j in range(i + 1, n):
            max_val = max(max_val, len(graph[i]) + len(graph[j]) - (1 if i in graph[j] else 0))
    return max_val
