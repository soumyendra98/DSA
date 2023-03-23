# 332, Using Hierholzer's Algorithm |O(N) and O(N)
from collections import defaultdict
from typing import List


class EulerianPath:
    def __init__(self, edges, start=None):
        self.start_node = start
        self.n = len(edges)
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.out_degree = defaultdict(int)
        self.path = []

        for f, t in edges:
            self.graph[f].append(t)
            self.in_degree[t] += 1
            self.out_degree[f] += 1
        self.vertices = list(self.graph.keys())

    def graphHasEulerianPath(self):
        start, end = 0, 0
        for i in self.vertices:
            if self.in_degree[i] - self.out_degree[i] > 1 or self.out_degree[i] - self.in_degree[i] > 1:
                return False
            elif self.in_degree[i] - self.out_degree[i] == 1:
                end += 1
            elif self.out_degree[i] - self.in_degree[i] == 1:
                start += 1
        return (end == 0 and start == 0) or (end == 1 and start == 1)

    def findStartNode(self):
        if self.start_node is None:
            for i in self.vertices:
                if self.out_degree[i] - self.in_degree[i] == 1:
                    self.start_node = i
                    break
                if self.out_degree[i] > 0:
                    self.start_node = i
        return self.start_node

    def dfs(self, node):
        while self.out_degree[node] > 0:
            self.out_degree[node] -= 1
            next_node = self.graph[node][self.out_degree[node]]
            self.dfs(next_node)

        self.path.append(node)

    def getPath(self):
        self.dfs(self.findStartNode())
        if len(self.path) == self.n + 1:
            return self.path
        return None

    def sortEdges(self, reverse=False):
        for edges in self.graph.values():
            edges.sort(reverse=reverse)


def findItinerary(tickets: List[List[str]]) -> List[str]:
    eulerian = EulerianPath(tickets, "JFK")
    eulerian.sortEdges(True)
    return reversed(eulerian.getPath())