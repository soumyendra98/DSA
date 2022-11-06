# 118, Tabulaiton | O(N ^ 2) and O(N ^ 2)
from typing import List


def generate(numRows: int) -> List[List[int]]:
    output = []
    for i in range(numRows):
        curr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                curr.append(1)
            else:
                curr.append(output[i - 1][j] + output[i - 1][j - 1])
        output.append(curr)
    return output
