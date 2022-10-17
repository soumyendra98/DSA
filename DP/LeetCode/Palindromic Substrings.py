# 647, Using DP to optimize | O(N^2) and O(N^2)
# dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
def countSubstrings(s: str) -> int:
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    count = len(s)

    for i in range(len(s)):
        dp[i][i] = True

    for i in range(len(s) - 1):
        dp[i][i + 1] = s[i] == s[i + 1]
        count += 1 if dp[i][i + 1] else 0

    for dist in range(2, len(s)):
        for i in range(len(s) - dist):
            j = i + dist
            dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            count += 1 if dp[i][j] else 0

    return count
