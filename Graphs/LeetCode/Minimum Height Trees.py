# 310, Topological Sort | O(N) and O(N)
from typing import List
from collections import defaultdict, deque


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(set)
    degrees = defaultdict(int)
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)
        degrees[x] += 1
        degrees[y] += 1

    queue = deque([i for i in range(n) if degrees[i] <= 1])

    output = []

    while queue:
        output = []
        for _ in range(len(queue)):
            output.append(queue.popleft())

        for node in output:
            degrees[node] -= 1
            for next_node in graph[node]:
                degrees[next_node] -= 1
                if degrees[next_node] == 1:
                    queue.append(next_node)

    return output
