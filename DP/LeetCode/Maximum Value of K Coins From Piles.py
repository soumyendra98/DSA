# 2218, DP | O(n * m) and O(m * n)

from typing import List
from functools import  cache
def maxValueOfCoins(piles: List[List[int]], k: int) -> int:
    n = len(piles)

    @cache
    def dp(i, k):
        if i == n or k == 0:
            return 0
        out, val = dp(i + 1, k), 0
        for j in range(min(k, len(piles[i]))):
            val += piles[i][j]
            out = max(out, val + dp(i + 1, k - j - 1))
        return out

    return dp(0, k)