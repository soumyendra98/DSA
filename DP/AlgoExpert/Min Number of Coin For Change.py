# DP | O(N * D) and O(N)
# dp[i] = min(dp[i], dp[i - coin] + 1) for all n + 1 > i >= coin
from typing import List


def minNumberOfCoinsForChange(n: int, denoms: List[int]) -> int:
    # Write your code here.
    if n == 0:
        return 0
    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0

    for coin in denoms:
        for i in range(coin, n + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[n] if dp[n] != float('inf') else -1