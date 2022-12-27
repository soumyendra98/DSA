#1167, Heap | O(N * log(N)) and O(N)
from typing import List
from heapq import heappop, heappush


def connectSticks(sticks: List[int]) -> int:
    heap = sorted(sticks)
    cost = 0
    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)

        cost += node1 + node2

        heappush(heap, node1 + node2)
    return cost
