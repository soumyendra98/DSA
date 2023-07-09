# 983, Memoization | O(Max(Arr)) and O(Max(Arr))
from typing import List

def mincostTickets(days: List[int], costs: List[int]) -> int:
    last_day = days[-1]
    days = set(days)
    dp = [0 for _ in range(last_day + 1)]
    for d in range(1, last_day + 1):
        if d not in days:
            dp[d] = dp[d - 1]
        else:
            dp[d] = min(dp[d - 1] + costs[0], dp[max(0, d - 7)] + costs[1], dp[max(0, d - 30)] + costs[2])
    return dp[last_day]
