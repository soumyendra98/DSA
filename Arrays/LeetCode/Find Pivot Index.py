# 724, Running Sum and Two pointer | O(N) and O(1)
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = 0
        left_sum = 0

        for index in range(len(nums)):
            right_sum += nums[index]

        for index in range(len(nums)):
            right_sum -= nums[index]
            if left_sum == right_sum:
                return index
            left_sum += nums[index]
        return -1


arr = [2, 1, -1]

sol = Solution()
print(sol.pivotIndex(arr))
