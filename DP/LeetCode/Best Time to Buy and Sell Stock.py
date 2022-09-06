# 121, DP | O(N) and O(1)
from typing import List


# Using Kadane's Algorithm
def maxProfit1(self, prices: List[int]) -> int:
    if len(prices) == 0:
        return 0
    profit = 0
    min_buy = prices[0]
    for i in range(len(prices)):
        min_buy = min(prices[i], min_buy)
        diff = prices[i] - min_buy
        profit = max(profit, diff)
    return profit


# Using DP (Two Pointer)
def maxProfit2(prices: List[int]) -> int:
    profit = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
            right += 1
        else:
            diff = prices[right] - prices[left]
            profit = max(diff, profit)
            right += 1
    return profit


arr = [7, 1, 5, 3, 6, 4]
print(maxProfit1(arr))
