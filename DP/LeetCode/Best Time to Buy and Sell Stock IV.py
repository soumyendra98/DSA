# Tabulation of all Possible Profits | O(N*K) and O(N*K)
from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    if not len(prices):
        return 0

    profits = [[0 for i in prices] for j in range(k + 1)]

    for t in range(1, k + 1):
        max_val = float("-inf")
        for idx in range(1, len(prices)):
            max_val = max(profits[t - 1][idx - 1] - prices[idx - 1], max_val)
            profits[t][idx] = max(profits[t][idx - 1], max_val + prices[idx])
    return profits[-1][-1]

