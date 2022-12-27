# 59, Simulation | O(N ^ 2) and O(N ^ 2)
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    start_row = 0
    end_row = n - 1
    start_col = 0
    end_col = n - 1

    output = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    while start_row <= end_row and start_col <= end_col:
        for j in range(start_col, end_col + 1):
            output[start_row][j] = num
            num += 1

        for i in range(start_row + 1, end_row + 1):
            output[i][end_col] = num
            num += 1
        for j in range(end_col - 1, start_col - 1, -1):
            if start_row == end_row:
                break
            output[end_row][j] = num
            num += 1

        for i in range(end_row - 1, start_row, -1):
            if end_col == start_col:
                break
            output[i][start_col] = num
            num += 1
        print(output)
        start_col += 1
        start_row += 1
        end_col -= 1
        end_row -= 1

    return output
