# 70, Memoization | O(N) and O(N)
from functools import cache


def climbStairs(n: int) -> int:
    @cache
    def dp(n):
        if n <= 2:
            return n

        return dp(n - 1) + dp(n - 2)

    return dp(n)
