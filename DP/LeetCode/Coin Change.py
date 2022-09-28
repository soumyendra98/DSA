# 322, DP - Bottom Up | O(N * C) and O(N)
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = [float('inf') for _ in range(amount + 1)]

    dp[0] = 0

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
