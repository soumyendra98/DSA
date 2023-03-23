# 1962, Using Max Heap | O(N * Log(N)) and O(N)
from heapq import heappop, heappush
from typing import List


def minStoneSum(piles: List[int], k: int) -> int:
    total = sum(piles)
    piles = [-val for val in piles]

    piles.sort()

    for i in range(k):
        temp = heappop(piles)
        total -= (-temp) // 2
        heappush(piles, temp + (-temp // 2))

    return total
