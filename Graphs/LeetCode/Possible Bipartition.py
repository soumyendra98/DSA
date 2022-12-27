# 886,
from collections import defaultdict, deque
from typing import List

def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    if len(dislikes) == 0:
        return True
    graph = defaultdict(set)
    colors = {i: -1 for i in range(1, n + 1)}
    for i, j in dislikes:
        graph[i].add(j)
        graph[j].add(i)

    for i in range(1, n + 1):
        if colors[i] == -1:
            queue = deque([(i, 0)])

            while queue:
                node, color = queue.popleft()

                for val in graph[node]:
                    if colors[val] == color:
                        return False
                    if colors[val] == -1:
                        colors[val] = 0 if color == 1 else 1
                        queue.append((val, colors[val]))

    return True
