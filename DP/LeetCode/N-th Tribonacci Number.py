# 1137, Memoization | O(N) and O(N)
from functools import cache


def tribonacci(n: int) -> int:
    @cache
    def dp(n):
        if n <= 1:
            return n
        if n == 2:
            return 1

        return dp(n - 1) + dp(n - 2) + dp(n - 3)

    return dp(n)
