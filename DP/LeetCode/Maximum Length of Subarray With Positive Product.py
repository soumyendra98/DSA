# 1567, Tabulation | O(N) and O(N)
from typing import List


def getMaxLen(nums: List[int]) -> int:
    pos_count = neg_count = output = 0
    for idx in range(1, len(nums)):
        if nums[idx] > 0:
            pos_count += 1
            neg_count += 1 if neg_count > 0 else 0
        elif nums[idx] < 0:
            pos_count, neg_count = neg_count + 1 if neg_count > 0 else 0, pos_count + 1
        else:
            pos_count = neg_count = 0

        if pos_count > output:
            output = pos_count
    return output
