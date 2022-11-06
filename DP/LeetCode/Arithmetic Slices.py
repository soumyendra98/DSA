# 413, Tabulation | O(N) and O(1)
from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:
    n = len(nums)
    prev = 0
    curr_len = 2
    curr = 0
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            curr_len += 1
            curr = prev + curr_len - 2
        else:
            curr_len = 2
            curr = prev
        prev = curr
    return curr
