# 931, Space Optimized Tabulation | O(N * N) and O(N)
from typing import List


def minFallingPathSum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    row_0 = [0] * n
    row_1 = matrix[n - 1]

    for i in reversed(range(n - 1)):
        for j in range(n):
            temp = []
            if 0 <= j - 1 < n:
                temp.append(row_1[j - 1])
            temp.append(row_1[j])
            if 0 <= j + 1 < n:
                temp.append(row_1[j + 1])

            row_0[j] = min(temp) + matrix[i][j]
        row_1 = row_0[:]

    return min(row_1)
