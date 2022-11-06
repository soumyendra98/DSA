# 120, Space Optimized Tabulation | O(N * N) and O(N)
from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    n = len(triangle)
    row_0 = [0] * n
    row_1 = triangle[n - 1]
    for i in reversed(range(n - 1)):
        for j in range(i + 1):
            temp = [row_1[j]]
            if 0 <= j + 1 < i + 2:
                temp.append(row_1[j + 1])

            row_0[j] = min(temp) + triangle[i][j]

        row_1 = row_0[:]

    return row_1[0]
