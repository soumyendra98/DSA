# Tabulation of all the possible profits | O(N) and O(N)
from typing import List


def maxProfit(prices: List[int]) -> int:
    if not len(prices):
        return 0

    profits = [[0 for i in prices] for k in range(3)]

    for t in range(1, 3):
        max_val = float("-inf")
        for idx in range(1, len(prices)):
            max_val = max(profits[t - 1][idx - 1] - prices[idx - 1], max_val)
            profits[t][idx] = max(profits[t][idx - 1], max_val + prices[idx])
    return profits[-1][-1]