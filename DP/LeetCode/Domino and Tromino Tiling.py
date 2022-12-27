# 790, Fibonacci Series Like | O(N) and O(N)

def numTilings(n: int) -> int:
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] * 2 + dp[i - 3]

    return dp[n] % (10 ** 9 + 7)
