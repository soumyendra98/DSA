# 416, DP | O(N) and O(sum(N) / 2)
# Calculate the subset sum and then check for all possible values that can be made using current val.
from typing import List


def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    subset_sum = total_sum // 2
    dp = [False] * (subset_sum + 1)
    dp[0] = True
    for i in range(len(nums)):
        for j in range(subset_sum, nums[i] - 1, -1):
            dp[j] = dp[j] or dp[j - nums[i]]

    return dp[subset_sum]
