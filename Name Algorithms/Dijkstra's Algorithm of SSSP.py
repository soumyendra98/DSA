# Dijkstra's Algorithms for single source shortest path | O(E * log(V)) and O(V)
from collections import defaultdict
from heapq import heappop, heappush


class Dijkstras:

    def __init__(self, edges, start):
        self.start = start
        self.graph = defaultdict(set)
        self.noNegative = True
        for origin, to, weight in edges:
            self.graph[origin].add((weight, to))
            if weight < 0:
                self.noNegative = False
                break
        self.n = len(self.graph.keys())

    def getCostOfShortestPath(self):
        if not self.noNegative:
            return -1

        heap = [(0, self.start)]
        visited = set()

        while heap:
            cost, node = heappop(heap)
            visited.add(node)

            if len(visited) == self.n:
                return cost

            for w, next_node in self.graph[node]:
                if next_node not in visited:
                    heappush(heap, (cost + w, next_node))
        return -1

    def getShortestPathMatrix(self):
        if not self.noNegative:
            return {}
        heap = [(0, self.start)]
        paths = {}

        while heap:
            cost, node = heappop(heap)
            paths[node] = cost

            if len(paths) == self.n:
                return paths

            for w, next_node in self.graph[node]:
                if next_node not in paths:
                    heappush(heap, (cost + w, next_node))
        return {}
