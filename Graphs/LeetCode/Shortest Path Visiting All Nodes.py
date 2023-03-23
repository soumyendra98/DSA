# 847, BFS + Bitmask | O((2 ^ N) * (N ^ 2)) and O((2 ^ N) * N)
from collections import deque
from typing import List


def shortestPathLength(graph: List[List[int]]) -> int:
    n = len(graph)

    if n == 1:
        return 0

    end_mask = (1 << n) - 1
    queue = deque([(i, 1 << i) for i in range(n)])
    distance = 0
    visited = set(queue)
    while queue:
        distance += 1
        for i in range(len(queue)):
            node, mask = queue.popleft()
            for next_node in graph[node]:
                next_mask = mask | (1 << next_node)
                if next_mask == end_mask:
                    return distance
                if (next_node, next_mask) not in visited:
                    visited.add((next_node, next_mask))
                    queue.append((next_node, next_mask))
