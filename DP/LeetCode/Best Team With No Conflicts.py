# 1626, Tabulation | O(N ^ 2) and O(N)
from typing import List


def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    dp = [0 for _ in range(len(scores))]
    max_val = 0
    sorted_ages = sorted(zip(ages, scores))
    for i in range(len(sorted_ages)):
        dp[i] = sorted_ages[i][1]
        for j in range(i):
            if sorted_ages[i][1] < sorted_ages[j][1]:
                continue
            dp[i] = max(dp[i], sorted_ages[i][1] + dp[j])
        max_val = max(dp[i], max_val)
    return max_val

