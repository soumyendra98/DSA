# 2477, DFS | O(N) and O(N)
from collections import defaultdict
from typing import List


def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    graph = defaultdict(list)

    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    total = [0]

    def dfs(curr, prev):
        people = 1
        for val in graph[curr]:
            if val == prev:
                continue
            people += dfs(val, curr)
        if curr != 0:
            total[0] += (people // seats) + (1 if people % seats else 0)

        return people

    dfs(0, 0)
    return total[0]
