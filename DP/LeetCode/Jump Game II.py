# 45, Memoization | O(N + M) and O(N) where M is the time needed to calculate the min of the sub array (arr[i: i + j])
from typing import List


def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    dp = [float('inf') for _ in range(n)]

    for i in reversed(range(n - 1)):
        j = nums[i]
        if j + i >= n - 1:
            dp[i] = 1
        else:
            dp[i] = min(dp[i: i + j + 1]) + 1

    return dp[0]
