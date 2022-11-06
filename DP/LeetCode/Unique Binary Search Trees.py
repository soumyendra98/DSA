# 96, Left + Right Subtree Tabulation | O(N ^ 2) and O(N)
# CATALAN's Number Method is O(N) and O(1)

def numTrees(n: int) -> int:
    # dp = [0 for _ in range(n + 1)]
    # dp[0] = dp[1] = 1

    # for i in range(2, n + 1):
    #     for j in range(i + 1):
    #         dp[i] += dp[i - j] * dp[j - 1]

    # return dp[n]

    catalan = 1
    for i in range(n):
        catalan = catalan * (2 * (2 * i + 1)) // (i + 2)
    return catalan

