# Bellman Ford Algorithm for finding Single Source Shortest Path
from collections import defaultdict


class BellmanFord:
    def __init__(self, edges, src, k = float('inf')):
        self.edges = edges
        self.graph = defaultdict(set)
        self.distances = defaultdict(lambda: float('inf'))
        self.src = src
        self.negativeCycle = None
        for origin, to, weight in edges:
            self.graph[origin].add((weight, to))

        self.vertices = self.graph.keys()
        self.n = len(self.vertices)
        self.k = k

    def calculateDistances(self):
        self.distances[self.src] = 0

        for _ in range(min(self.n - 1, self.k)):
            for u, v, w in self.edges:
                if self.distances[u] != float("Inf") and self.distances[u] + w < self.distances[v]:
                    self.distances[v] = self.distances[u] + w

    def isNegativeCycle(self):
        if len(self.distances.keys()) != self.n:
            self.calculateDistances()
        if self.negativeCycle is None:
            for u, v, w in self.edges:
                if self.distances[u] != float("Inf") and self.distances[u] + w < self.distances[v]:
                    print("Graph contains negative weight cycle")
                    self.negativeCycle = True
                    return self.negativeCycle
            self.negativeCycle = False
        return self.negativeCycle

    def getShortestPathMatrix(self):
        if self.isNegativeCycle():
            return {}
        else:
            return self.distances

    def getCostOfShortestPath(self):
        if self.isNegativeCycle():
            return -1
        else:
            cost = 0
            for key in self.distances.keys():
                cost += self.distances[key]
            return cost


