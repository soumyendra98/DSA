# 221, Tabulation | O(N * M) and O(N * M)
from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    max_val = 0
    for i in range(m):
        for j in range(n):
            if j == 0 or i == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == '1':
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            if dp[i][j] > max_val:
                max_val = dp[i][j]
    return max_val ** 2
