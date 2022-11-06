# 1314, Prefix sum | O(N * M) and O(N * M)
# dp[i][j] = pre[i + k][j +k] - pre[i + k][j - k] - pre[i - k][j + k] + pre[i - k][j - k]
from typing import List


def matrixBlockSum(mat: List[List[int]], k: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        curr = 0
        for j in range(n):
            curr += mat[i][j]
            mat[i][j] = curr

    for j in range(n):
        curr = 0
        for i in range(m):
            curr += mat[i][j]
            mat[i][j] = curr

    for i in range(m):
        x_min = max(0, i - k)
        x_max = min(m - 1, i + k)
        for j in range(n):
            y_min = max(0, j - k)
            y_max = min(n - 1, j + k)
            dp[i][j] += mat[x_max][y_max]

            if y_min - 1 >= 0:
                dp[i][j] -= mat[x_max][y_min - 1]
            if x_min - 1 >= 0:
                dp[i][j] -= mat[x_min - 1][y_max]
            if x_min - 1 >= 0 and y_min - 1 >= 0:
                dp[i][j] += mat[x_min - 1][y_min - 1]

    return dp
