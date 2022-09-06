# 1480, Running Sum | O(N) and O(1)

from typing import List


# Inplace Running Sum | O(N) and O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        for index in range(len(nums)):
            running_sum += nums[index]
            nums[index] = running_sum
        return nums
