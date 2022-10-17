# 1335, Using memoization to optimize from the last day | O((N ^ 2) * D) and O(N * D)
from typing import List
from functools import lru_cache


def minDifficulty(jobDifficulty: List[int], d: int) -> int:
    n = len(jobDifficulty)

    if d > n:
        return - 1

    @lru_cache(None)
    def dp(i, j):
        if j == d:
            return max(jobDifficulty[i:])

        diff = float('inf')
        max_val = -1
        for idx in range(i, n - d + j):
            if jobDifficulty[idx] > max_val:
                max_val = jobDifficulty[idx]

            diff = min(diff, max_val + dp(idx + 1, j + 1))
        return diff

    return dp(0, 1)
