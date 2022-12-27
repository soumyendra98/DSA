# 2256, Double Pass | O(N) and O(1)
from typing import List


def minimumAverageDifference(nums: List[int]) -> int:
    n = len(nums)
    right_sum = sum(nums)
    left_sum = 0
    min_val = float('inf')
    min_idx = -1

    for i in range(n - 1):
        left_sum += nums[i]
        right_sum -= nums[i]
        val = abs((left_sum // (i + 1)) - (right_sum // (n - i - 1)))
        if val < min_val:
            min_val = val
            min_idx = i

    if (left_sum + right_sum) // n < min_val:
        return n - 1
    return min_idx
