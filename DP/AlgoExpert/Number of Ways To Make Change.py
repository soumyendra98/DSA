# DP | O(N * D) and O(N)
# dp[0] = 1 --> Base Case
# for all j's > denoms[i] --> increase the dp[j] by dp[j - denoms[i]]

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    d = len(denoms)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(d):
        for j in range(n+1):
            if j >= denoms[i]:
                dp[j] += dp[j - denoms[i]]
    return dp[n]
