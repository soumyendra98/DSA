# 240, Search Space Reduction | O(log(N) * log(M)) and O(1)
import bisect
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    r_idx = bisect.bisect_left(matrix[0], target)

    if r_idx != n and matrix[0][r_idx] == target:
        return True

    for i in range(1, m):
        c_idx = bisect.bisect_left(matrix[i][: r_idx], target)
        if c_idx != n and matrix[i][c_idx] == target:
            return True

    return False
