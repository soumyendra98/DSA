# 974, Remainder and Hashtable | O(N) and O(1)
from typing import List


def subarraysDivByK(nums: List[int], k: int) -> int:
    prefix = 0
    rem_count = [0] * k
    rem_count[0] = 1
    total = 0
    for num in nums:
        prefix = (prefix + num) % k
        total += rem_count[prefix]
        rem_count[prefix] += 1
    return total
