# Using Max heap | O(NlogN) and O(N)
from heapq import heappop, heappush, heapify
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    if len(stones) == 1:
        return stones[0]

    heap = [stone * -1 for stone in stones]
    heapify(heap)

    while len(heap) > 1:
        num1 = -1 * heappop(heap)
        num2 = -1 * heappop(heap)
        if num1 != num2:
            heappush(heap, -1 * (num1 - num2))

    if len(heap) == 0:
        return 0

    return -1 * heap[0]
