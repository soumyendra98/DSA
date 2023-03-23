from collections import defaultdict, deque


class SPFA:
    def __init__(self, edges, src):
        self.edges = edges
        self.graph = defaultdict(set)
        self.distances = defaultdict(lambda: float('inf'))
        self.src = src
        self.disjoint = False
        for origin, to, weight in edges:
            self.graph[origin].add((weight, to))

        self.vertices = self.graph.keys()
        self.n = len(self.vertices)
        self.calculateShortestDistances()

    def calculateShortestDistances(self):
        visited = defaultdict(lambda: False)
        queue = deque([self.src])
        visited[self.src] = True

        while queue:
            node = queue.popleft()
            visited[node] = False

            for next_node, weight in self.graph[node]:
                if self.distances[next_node] > self.distances[node] + weight:
                    self.distances[next_node] = self.distances[node] + weight
                    if not visited[next_node]:
                        queue.append(next_node)
                        visited[next_node] = True
        for value in visited.values():
            if not value:
                self.disjoint = True
                break

    def getShortestPathMatrix(self):
        if self.disjoint:
            return {}
        else:
            return self.distances

    def getCostOfShortestPath(self):
        if self.disjoint:
            return -1
        else:
            cost = 0
            for key in self.distances.keys():
                cost += self.distances[key]
            return cost
