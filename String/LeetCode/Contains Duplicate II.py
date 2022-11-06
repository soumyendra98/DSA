# 219, Hashmap | O(N) and O(N)
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    idx_map = {}
    for idx in range(len(nums)):
        if nums[idx] in idx_map and idx - idx_map[nums[idx]] <= k:
            return True
        idx_map[nums[idx]] = idx
    return False
