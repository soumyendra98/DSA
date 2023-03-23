# MST using Kruskal's Algorithm
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
                self.rank[ry] += self.rank[rx]
            else:
                self.uf[ry] = rx
                self.rank[rx] += self.rank[ry]
            return True
        return False


class Kruskals:
    def __int__(self, n, edges):
        graph = defaultdict(int)

        for x, y, w in edges:
            graph[(x, y)] = w

        heap = sorted(graph.keys(), key=lambda x: graph[x])

        self.uf = UF(n)
        self.cost = 0
        self.edges = []
        for i, j in heap:
            if self.uf.find(i) != self.uf.find(j):
                self.uf.union(i, j)
                self.edges.append((i, j))
                self.cost += graph[(i, j)]

    def mstCost(self):
        return self.cost

    def mstEdge(self):
        return self.edges
