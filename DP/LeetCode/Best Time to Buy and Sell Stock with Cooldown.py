# 309, Three States | O(N) and O(1)
from typing import List


def maxProfit(prices: List[int]) -> int:
    buy = -prices[0]
    profit = 0
    cooldown = 0

    for i in range(1, len(prices)):
        print(buy, cooldown, profit)
        prev_profit = profit
        profit = max(profit, buy + prices[i])
        buy = max(buy, cooldown - prices[i])
        cooldown = max(cooldown, prev_profit)

    return profit
