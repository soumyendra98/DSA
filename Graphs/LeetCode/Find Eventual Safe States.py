# 802, Topological Sort | O(N) and O(N)
from collections import deque
from typing import List


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    rev_graph = [[] for _ in range(n)]
    in_degree = [0 for _ in range(n)]

    for i in range(n):
        for node in graph[i]:
            rev_graph[node].append(i)
            in_degree[i] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    output = []
    while queue:
        node = queue.popleft()
        output.append(node)

        for next_node in rev_graph[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)

    output.sort()

    return output
