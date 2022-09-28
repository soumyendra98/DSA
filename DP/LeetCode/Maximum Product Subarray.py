# 152, Kadane's Algorithm | O(N) and O(1)
from typing import List


def maxProduct(nums: List[int]) -> int:
    dp = []
    max_prod = nums[0]
    curr_max = curr_min = 1
    for idx in range(len(nums)):
        curr_max, curr_min = max(curr_max * nums[idx], curr_min * nums[idx], nums[idx]), min(curr_max * nums[idx],
                                                                                             curr_min * nums[idx],
                                                                                             nums[idx])
        max_prod = max(curr_max, max_prod)

    return max_prod
