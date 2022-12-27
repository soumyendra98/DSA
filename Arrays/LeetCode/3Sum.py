# 15, Sort + Two Sum | O(N ^ 2) and O(N)
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    output = set()

    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == 0:
                output.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif curr_sum > 0:
                right -= 1
            else:
                left += 1
    return [list(val) for val in output]
