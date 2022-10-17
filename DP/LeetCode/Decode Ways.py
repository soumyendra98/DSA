# 91, Using Memoization | O(N) and O(N)

def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    dp[0], dp[1] = 1, 1

    for idx in range(2, len(s) + 1):
        if s[idx - 1] != '0':
            dp[idx] = dp[idx - 1]

        if s[idx - 1] == '0' and s[idx - 2] == '0':
            return 0

        if 10 <= int(s[idx - 2] + s[idx - 1]) <= 26:
            dp[idx] += dp[idx - 2]

    return dp[len(s)]
