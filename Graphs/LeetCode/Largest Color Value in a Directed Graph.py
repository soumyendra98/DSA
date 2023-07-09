# 1857, Topological Sort + DP | O(N) and O(N)

from collections import defaultdict, deque
from typing import List

def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1

    starting_nodes = [i for i in range(n) if indegree[i] == 0]
    queue = deque(starting_nodes)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    if len(order) != n:
        return -1

    output = 0
    counts = [defaultdict(int) for _ in range(n)]

    colors_set = set([chr(i) for i in range(97, 123)])

    for i in range(n - 1, -1, -1):
        node = order[i]
        best = defaultdict(int)
        for next_node in graph[node]:
            for c in colors_set:
                best[c] = max(best[c], counts[next_node][c])
        best[colors[node]] += 1
        counts[node] = best
    for node in starting_nodes:
        output = max(output, max(counts[node].values()))
    return output
