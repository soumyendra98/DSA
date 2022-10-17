# 976, Simple Math | O(NlogN) and O(1)
from typing import List


def largestPerimeter(nums: List[int]) -> int:
    nums.sort()

    def check(x, y, z):
        if x >= y + z:
            return False
        return True

    for idx in reversed(range(2, len(nums))):
        if check(nums[idx], nums[idx - 1], nums[idx - 2]):
            return nums[idx] + nums[idx - 1] + nums[idx - 2]

    return 0
