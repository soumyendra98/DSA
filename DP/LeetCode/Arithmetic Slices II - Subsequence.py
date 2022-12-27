# 446, Tabulation | O(N ^ @) and O(N ^ 2)
# Maintain a Counter for the number of AS's ending at the current index and with the current difference
# [
#   idx:
#       {
#           diff: count
#           ....
#       }
#   ....
# ]
from typing import List
from collections import Counter


def numberOfArithmeticSlices(nums: List[int]) -> int:
    n = len(nums)
    dp = [Counter() for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(i):
            diff = nums[j] - nums[i]
            total += dp[j][diff]
            dp[i][diff] += dp[j][diff] + 1

    return total
