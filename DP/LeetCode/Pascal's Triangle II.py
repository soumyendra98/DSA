# 119, Tabulation Space Optimized | O(N ^ 2) and O(N)
from typing import List


def getRow(rowIndex: int) -> List[int]:
    prev = []

    for i in range(rowIndex + 1):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(prev[j] + prev[j - 1])
        prev = temp
    return prev
