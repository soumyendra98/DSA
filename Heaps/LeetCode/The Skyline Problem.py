# 218, Using Sweep line and Max Heap | O(NlogN) and O(N)
#
from heapq import heappop, heappush
from typing import List


def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    output = []
    heap = []
    index = 0
    while index < len(buildings) or heap:
        if not heap or index < len(buildings) and buildings[index][0] <= -heap[0][1]:
            start = buildings[index][0]
            while index < len(buildings) and buildings[index][0] == start:
                heappush(heap, (-buildings[index][2], -buildings[index][1]))
                index += 1
        else:
            start = -heap[0][1]
            while heap and -heap[0][1] <= start:
                heappop(heap)

        height = len(heap) and -heap[0][0]
        if len(output) == 0 or height != output[-1][1]:
            output.append([start, height])

    return output

