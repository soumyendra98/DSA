# 139, Tabulation of the string s | O(N ^ 2) and O(N)
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    word_set = set(wordDict)
    dp = [False for _ in range(n + 1)]
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j: i] in word_set:
                dp[i] = True
                break
    return dp[n]
