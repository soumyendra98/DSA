# 55 Simple Tabulation | O(N) and O(1)
from typing import List


def canJump(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True

    max_val = 0

    for i in range(n - 1):
        if max_val < i:
            return False
        max_val = max(max_val, nums[i] + i)

    if max_val >= n - 1 and nums[0] != 0:
        return True
    return False
