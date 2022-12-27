# 279, Tabulation | O(N ^ 2) and O(N)
def numSquares(n: int) -> int:
    dp = [float('inf') for _ in range(n + 1)]
    num = 1

    dp[0] = 0

    while num ** 2 <= n:
        for j in range(num ** 2, n + 1):
            dp[j] = min(dp[j], dp[j - num ** 2] + 1)
        num += 1
    return dp[n] if dp[n] != float('inf') else 1
