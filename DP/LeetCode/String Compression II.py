# 1531, Memoization using previous character, char count and deletions | O(N * K ^ 2 ) and O(N * K ^ 2)
from functools import lru_cache


def getLengthOfOptimalCompression(s: str, k: int) -> int:
    @lru_cache(None)
    def dp(idx, prev, char_count, deletions):
        if deletions < 0:
            return float('inf')
        if idx == len(s):
            return 0

        delete_count = dp(idx + 1, prev, char_count, deletions - 1)
        if s[idx] == prev:
            keep_count = dp(idx + 1, prev, char_count + 1, deletions)
            if char_count in {1, 9, 99}:
                keep_count += 1
        else:
            keep_count = dp(idx + 1, s[idx], 1, deletions) + 1

        return min(keep_count, delete_count)

    return dp(0, "", 0, k)
