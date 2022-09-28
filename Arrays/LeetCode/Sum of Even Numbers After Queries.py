# 985, Single Pass | O(N + Q) and O(Q)
from typing import List


def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    even_sum = 0
    output = []
    for num in nums:
        if num % 2 == 0:
            even_sum += num

    for val, idx in queries:
        if nums[idx] % 2 == 0:
            even_sum -= nums[idx]
        nums[idx] += val
        if nums[idx] % 2 == 0:
            even_sum += nums[idx]
        output.append(even_sum)

    return output
