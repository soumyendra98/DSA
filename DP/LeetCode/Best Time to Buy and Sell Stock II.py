# Using Peak and Trough | O(N) and O(1)
from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0

    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx - 1]:
            profit += prices[idx] - prices[idx - 1]

    return profit

