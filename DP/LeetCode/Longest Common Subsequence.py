# 1143, Tabulation | O(N * M) and O(N * M)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    n = len(text1)
    m = len(text2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    output = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if output < dp[i][j]:
                output = dp[i][j]
    return output
