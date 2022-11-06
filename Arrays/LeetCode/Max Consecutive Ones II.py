# 497, Counting Ones and Zero's index | O(N) and O(1)
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    isZeroFound = False
    zero_index = -1
    count = 0
    max_count = 0

    for idx in range(len(nums)):
        if nums[idx] == 1:
            count += 1
        else:
            if isZeroFound:
                count = idx - zero_index
            else:
                count += 1
                isZeroFound = True
            zero_index = idx
        if count > max_count:
            max_count = count
    return max_count
