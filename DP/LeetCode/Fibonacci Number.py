# 509, Memoization | O(N) and O(N)
from functools import cache


def fib(n: int) -> int:
    @cache
    def dp(n):
        if n <= 1:
            return n
        return dp(n - 1) + dp(n - 2)

    return dp(n)

# Golden Ratio is also called Binet's formula
# def fib(N: int) -> int:
#        golden_ratio = (1 + (5 ** 0.5)) / 2
#        return int(round((golden_ratio ** N) / (5 ** 0.5)))
