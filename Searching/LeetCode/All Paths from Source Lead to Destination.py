# 1059, DFS with In Degree and Out Degree | O(N) and O(N)
from typing import List
from collections import defaultdict


def leadsToDestination(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    if source != destination and len(edges) == 0:
        return False

    for f, t in edges:
        graph[f].add(t)
        in_degree[t] += 1
        out_degree[f] += 1

    if out_degree[destination]:
        return False

    visited = set()
    stack = [source]
    destinations = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        for next_node in graph[node]:
            if node in graph[next_node]:
                return False
            stack.append(next_node)

        if out_degree[node] == 0:
            destinations.add(node)

    return len(destinations) == 1
