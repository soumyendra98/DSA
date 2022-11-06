# 645, Counter | O(N) and O(N)
from collections import Counter
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    num_count = Counter(nums)
    output = [-1, -1]
    for idx in range(1, n + 1):
        if idx not in num_count:
            output[1] = idx
        if num_count[idx] == 2:
            output[0] = idx
    return output
