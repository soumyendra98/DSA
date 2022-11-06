# 714, Two states | O(N) and O(1)
from typing import List


def maxProfit(prices: List[int], fee: int) -> int:
    profit = 0
    buy = -prices[0] 
    for i in range(1, len(prices)):
        profit = max(profit, buy + prices[i] - fee)
        buy = max(buy, profit - prices[i])
    return profit
