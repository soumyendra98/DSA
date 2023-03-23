# 785, Bipartite Check
from collections import deque
from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    colors = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            queue = deque([(i, 0)])
            colors[i] = 0
            while queue:
                node, color = queue.popleft()

                for next_node in graph[node]:
                    if colors[next_node] == color:
                        return False
                    if colors[next_node] == -1:
                        colors[next_node] = 1 - color
                        queue.append((next_node, 1 - color))
    return True
