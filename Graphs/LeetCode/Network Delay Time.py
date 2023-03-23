# 743, Dijsktra's Algorithm | O(E * log(N)) and O(N + E)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(set)

    for u, v, w in times:
        graph[u].add((w, v))

    heap = [(0, k)]
    visited = set()

    while heap:
        time, node = heappop(heap)
        visited.add(node)

        if len(visited) == n:
            return time

        for w, next_node in graph[node]:
            if next_node not in visited:
                heappush(heap, (time + w, next_node))

    return -1
