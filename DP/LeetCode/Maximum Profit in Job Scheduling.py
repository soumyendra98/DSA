# 1235, 0/1 Knapsack with Memoization and sorting| O(NlogN) and O(N)
from bisect import bisect_left as bisect
from typing import List


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(endTime)
    jobs = sorted(zip(startTime, endTime, profit))

    dp = [0 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        val = bisect(jobs, jobs[i][1], key=lambda x: x[0])
        dp[i] = max(dp[val] + jobs[i][2], dp[i + 1])
    return dp[0]
