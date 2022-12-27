# 2387, Binary Search | O(M * Log(N)) and O(1)
from bisect import bisect
from typing import List


def matrixMedian(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    flag = m * n // 2 + 1
    start = min(row[0] for row in grid)
    end = max(row[-1] for row in grid)

    while start < end:
        mid = (start + end) // 2
        total = 0

        for row in grid:
            total += bisect(row, mid)

        if total >= flag:
            end = mid
        else:
            start = mid + 1

    return end
