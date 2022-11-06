# 766, Simple diagonal Traversal | O(N * M) and O(1)
from typing import List


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        for i in range(1, n):
            if i + j == m:
                break
            if matrix[0][j] != matrix[i][i + j]:
                return False
    for i in range(1, n):
        for j in range(1, m):
            if i + j == n:
                break
            if matrix[i][0] != matrix[i + j][j]:
                return False
    return True
