# Created a table of current position of all balls:
from typing import List


def findBall(self, grid: List[List[int]]) -> List[int]:
    rows = len(grid)
    cols = len(grid[0])
    output = [val for val in range(cols)]

    for i in range(rows):
        for j, val in enumerate(output):
            if val != -1:
                if val + 1 < cols and grid[i][val] == 1 and grid[i][val + 1] == 1:
                    output[j] = val + 1
                elif val - 1 >= 0 and grid[i][val] == -1 and grid[i][val - 1] == -1:
                    output[j] = val - 1
                else:
                    output[j] = -1

    return output

