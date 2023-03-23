# 1443, DFS | O(N) and O(N)
from collections import  defaultdict
from typing import List


def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node, prev):
        res = 0
        for next_node in graph[node]:
            if prev != next_node:
                res += dfs(next_node, node)

        if hasApple[node] and node != 0:
            hasApple[prev] = True
            return res + 2

        return res

    return dfs(0, 0)
