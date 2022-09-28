# 815, Map the Stops and Buses and then use BFS on the Stops | O(N) and O(N ^ 2) where N is the total number of routes
# ie -> sum(routes[i])
from collections import defaultdict
from typing import List


def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    bus_map = defaultdict(set)

    for idx in range(len(routes)):
        for val in routes[idx]:
            bus_map[val].add(idx)

    queue = [(source, 0)]
    seen = set()

    for stop, bus in queue:
        if stop == target: return bus
        for i in bus_map[stop]:
            for j in routes[i]:
                if j not in seen:
                    seen.add(j)
                    queue.append((j, bus + 1))
            routes[i] = []
    return - 1
