# 1584, MST Using Kruskal's | O(N ^ 2 * log(N ^ 2)) and O(N ^ 2)
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n):
        self.uf = {i: i for i in range(n + 1)}
        self.rank = {i: 1 for i in range(n + 1)}

    def find(self, x):
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.uf[rx] = ry
                self.rank[ry] += self.rank[ry]
            else:
                self.uf[ry] = rx
                self.rank[rx] += self.rank[ry]
            return True
        return False


def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)
    graph = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            graph[(i, j)] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    heap = sorted(graph.keys(), key=lambda x: graph[x])

    uf = UF(n)
    cost = 0
    for i, j in heap:
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            cost += graph[(i, j)]
    return cost
