# 2128, Row == Rotation(row) | O(M * N) and O(M)
from typing import List


def removeOnes(grid: List[List[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])

    def flip(row):
        return [1 - val for val in row]

    start = grid[0]
    for i in range(1, m):
        if not (grid[i] == start or flip(grid[i]) == start):
            return False

    return True
