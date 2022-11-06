# 213, Take first or last and Tabulation | O(N) and O(1)
from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return max(nums)

    def check(arr):
        first = arr[0]
        second = max(arr[:2])
        for idx in range(2, n - 1):
            curr = max(first + arr[idx], second)
            first = second
            second = curr
        return second

    return max(check(nums[1:]), check(nums[: -1]))
