# Kadane's Algorithm | O(N) and O(1)
from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_till_now = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum > max_till_now:
            max_till_now = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_till_now
