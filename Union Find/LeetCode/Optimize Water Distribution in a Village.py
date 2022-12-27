# 1168, Using Kruskal's Algorithms with UF | O(E * log(E)) and O(E)
from typing import List
from collections import defaultdict


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


def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
    graph = defaultdict(int)

    for i in range(n):
        graph[(0, i + 1)] = wells[i]

    for x, y, w in pipes:
        graph[(x, y)] = w

    heap = sorted(graph.keys(), key=lambda k: graph[k])
    uf = UF(n)
    output = 0
    for i, j in heap:
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            output += graph[(i, j)]

    return output
