# 1216, Longest Palindromic Subsequence | O(N ^ 2) and O(N ^ 2)
def isValidPalindrome(s: str, k: int) -> bool:
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for char_len in range(2, n + 1):
        for i in range(n - char_len + 1):
            j = i + char_len - 1
            if s[i] == s[j] and char_len == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    if dp[0][n - 1] >= n - k:
        return True
    else:
        return False
