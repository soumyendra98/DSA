# 523, Prefix sum and Hashmap | O(N) and O(K)
from typing import List


def checkSubarraySum(nums: List[int], k: int) -> bool:
    num_map = {0: -1}
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum = (curr_sum + nums[i]) % k
        if curr_sum in num_map:
            if i - num_map[curr_sum] >= 2:
                return True
        else:
            num_map[curr_sum] = i

    return False

