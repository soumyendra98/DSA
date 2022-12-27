# 2488, Calculating the Difference of higher and lower values| O(N) and O(N)
from collections import Counter
from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    n = len(nums)
    diff_count = Counter([0])
    pre = 0
    count = 0
    found = False
    for val in nums:
        if val > k:
            pre += 1
        elif val < k:
            pre -= 1
        else:
            found = True
        if found:
            count += diff_count[pre] + diff_count[pre - 1]
        else:
            diff_count[pre] += 1
    return count
