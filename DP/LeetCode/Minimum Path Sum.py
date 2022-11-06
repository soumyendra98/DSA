# 64, Space optimized Tabulation | O(N * M) and O(N)
from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    prev = [0 for _ in range(n)]
    curr = [0 for _ in range(n)]

    for i in range(m):
        pre = 0
        for j in range(n):
            curr[j] = grid[i][j]
            if j == 0:
                curr[j] += prev[j]
            elif i == 0:
                curr[j] += curr[j - 1]
            else:
                curr[j] += min(prev[j], curr[j - 1])
        prev = curr[:]

    return curr[n - 1]
