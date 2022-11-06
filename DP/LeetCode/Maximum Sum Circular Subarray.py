# 918, Kadane's algorithm with minimum value | O(N) and O(1)
from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:
    max_val = float('-inf')
    min_val = float('inf')
    curr_max, curr_min = 0, 0
    total = 0
    for num in nums:
        curr_max += num
        curr_min += num
        if curr_max > max_val:
            max_val = curr_max
        if curr_min < min_val:
            min_val = curr_min
        if curr_max < 0:
            curr_max = 0
        if curr_min > 0:
            curr_min = 0

    total += num

    return max(max_val, total - min_val) if max_val > 0 else max_val
