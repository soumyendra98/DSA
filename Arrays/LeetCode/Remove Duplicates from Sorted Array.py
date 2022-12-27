# 26, Single Pass | O(N) and O(1)
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    idx = 1
    while idx < len(nums):
        if nums[idx] == nums[idx - 1]:
            nums.pop(idx)
        else:
            idx += 1
    return len(nums)