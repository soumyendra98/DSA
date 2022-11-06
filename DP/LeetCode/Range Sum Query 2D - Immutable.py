# 304, Prefix Sum Matrix Calculation | O(N * M) and O(1)
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = self.calculatePrefixSumMatrix(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr_sum = self.pre[row2][col2]

        if row1 - 1 >= 0:
            curr_sum -= self.pre[row1 - 1][col2]
        if col1 - 1 >= 0:
            curr_sum -= self.pre[row2][col1 - 1]
        if col1 - 1 >= 0 and row1 - 1 >= 0:
            curr_sum += self.pre[row1 - 1][col1 - 1]
        return curr_sum

    def calculatePrefixSumMatrix(self, mat: List[List[int]]):
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            pre = 0
            for j in range(m):
                pre += mat[i][j]
                mat[i][j] = pre
        for j in range(m):
            pre = mat[0][j]
            for i in range(1, n):
                pre += mat[i][j]
                mat[i][j] = pre
        return mat
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
