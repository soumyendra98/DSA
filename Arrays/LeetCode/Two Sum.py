# 1, Hash Table | O(N) and O(1)
from collections import defaultdict
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = defaultdict(lambda: -1)
    for idx, num in enumerate(nums):
        if num_dict[target - num] != -1:
            return [num_dict[target - num], idx]
        num_dict[num] = idx

    return [-1, -1]