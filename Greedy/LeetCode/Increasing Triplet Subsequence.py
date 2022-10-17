# 334, Simple 2 smallest | O(N) and O(1)
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    min_a = float('inf')
    min_b = float('inf')
    n = len(nums)
    for idx in range(n):
        if nums[idx] <= min_a:
            min_a = nums[idx]
        elif nums[idx] <= min_b:
            min_b = nums[idx]
        elif nums[idx] > min_a and nums[idx] > min_b:
            return True
    return False

