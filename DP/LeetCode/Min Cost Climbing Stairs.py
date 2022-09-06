# 746, DP (bottom up) | O(N) and O(1)
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    if len(cost) == 0:
        return min(cost)
    min0, min1 = cost[0], cost[1]

    for index in range(2, len(cost)):
        min0, min1 = min1, cost[index] + min(min0, min1)

    return min(min0, min1)


arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(arr))
