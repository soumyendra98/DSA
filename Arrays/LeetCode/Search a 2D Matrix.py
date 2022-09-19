# Finding the row and then the column |O(M + N) and O(1)
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][m - 1] > target:
            for j in range(m):
                if matrix[i][j] == target:
                    return True
            break
        elif matrix[i][m - 1] == target:
            return True

    return False

