# 1833, Sorting | O(N * Log(N)) and O(N)
from typing import List


def maxIceCream(costs: List[int], coins: int) -> int:
    costs.sort()
    total = 0
    for cost in costs:
        if coins - cost < 0:
            break
        coins -= cost
        total += 1
    return total
