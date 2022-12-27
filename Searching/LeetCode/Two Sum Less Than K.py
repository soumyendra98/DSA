# 1099, Sorting and two pointers | O(N * Log(N)) and O(1)
from typing import List


def twoSumLessThanK(nums: List[int], k: int) -> int:
    if len(nums) <= 1:
        return -1

    nums.sort()
    l = 0
    r = len(nums) - 1
    max_sum = -1

    while l < r:
        if nums[l] + nums[r] < k:
            if max_sum < nums[l] + nums[r]:
                max_sum = nums[l] + nums[r]
            l += 1
        else:
            r -= 1

    return max_sum
