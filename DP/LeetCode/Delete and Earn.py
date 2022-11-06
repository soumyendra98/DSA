# 740, Space Optimized Tabulation | O(N + max(nums)) and O(N)
from collections import defaultdict
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    num_count = defaultdict(int)
    max_val = 0
    for num in nums:
        num_count[num] += 1
        max_val = max(num, max_val)

    first = num_count[0]
    second = num_count[1]
    for idx in range(2, max_val + 1):
        curr = max(second, first + idx * num_count[idx])
        first = second
        second = curr
    return second
