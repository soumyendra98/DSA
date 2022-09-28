# 718 Using Bottom Up DP | O(M * N) and O(M * N)
from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    m = len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if nums1[i] == nums2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1

    return max(max(row) for row in dp)

