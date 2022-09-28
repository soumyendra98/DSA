# 198, DP | O(N) and O(1)
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    first = nums[0]
    second = max(nums[0], nums[1])

    for idx in range(2, len(nums)):
        curr = max(first + nums[idx], second)
        first = second
        second = curr

    return second
