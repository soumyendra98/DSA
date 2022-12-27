# MST using Prims Algorithm
from collections import defaultdict
from heapq import heappop, heappush


class Prims:
    def __int__(self, n, edges):
        self.graph = defaultdict(set)

        for x, y, w in edges:
            self.graph[x].add((w, y))
            self.graph[y].add((w, x))

        heap = [(0, 0, 0)]
        visited = set()
        self.cost = 0
        self.edges = []

        while heap and len(visited) <= n:
            cost, prev, vertex = heappop(heap)

            if vertex in visited:
                continue

            visited.add(vertex)
            self.cost += cost
            self.edges.append((prev, vertex))

            for w, y in self.graph[vertex]:
                heappush(heap, (w, vertex, y))

    def mstCost(self):
        return self.cost

    def mstEdge(self):
        return self.edges


