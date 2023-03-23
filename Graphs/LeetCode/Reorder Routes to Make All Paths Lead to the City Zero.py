# 1466, DFS | O(N) and O(N)
from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
    graph = [[] for _ in range(n)]

    for a, b in connections:
        graph[a].append((b, 0))
        graph[b].append((a, 1))

    stack = [(0, 1)]
    visited = {0}
    count = 0
    while stack:
        node, direction = stack.pop()
        if not direction:
            count += 1
        for next_node, new_dir in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                stack.append((next_node, new_dir))
    return count
