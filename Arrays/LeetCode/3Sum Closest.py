# 16, Two Pointer with One element fixed | O(N^2) and O(1)
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    min_diff = float('inf')
    for idx in range(len(nums)):
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[idx] + nums[left] + nums[right]
            if curr_sum == target:
                return curr_sum

            if abs(target - curr_sum) < abs(min_diff):
                min_diff = target - curr_sum

            if curr_sum < target:
                left += 1
            else:
                right -= 1

    return target - min_diff
