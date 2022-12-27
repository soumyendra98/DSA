# 797, DFS | O(N) and O(N)
from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    stack = [(0, [])]
    paths = []
    while stack:
        node, path = stack.pop()
        path.append(node)

        if node == len(graph) - 1:
            paths.append(path)
            continue

        for next_node in graph[node]:
            stack.append((next_node, path[:]))
    return paths
