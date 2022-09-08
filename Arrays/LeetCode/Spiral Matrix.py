# Simple Spiral Traversal using bound | O(N*M) and O(N*M)
from typing import List


def spiralOrder(self, array: List[List[int]]) -> List[int]:
    # Write your code here.
    iMax = len(array) - 1
    jMax = len(array[0]) - 1
    iMin = 0
    jMin = 0
    output = []

    while iMin <= iMax and jMin <= jMax:
        for j in range(jMin, jMax + 1):
            output.append(array[iMin][j])
        for i in range(iMin + 1, iMax + 1):
            output.append(array[i][jMax])
        for j in reversed(range(jMin, jMax)):
            if iMin == iMax:
                break
            output.append(array[iMax][j])
        for i in reversed(range(iMin + 1, iMax)):
            if jMin == jMax:
                break
            output.append(array[i][jMin])

        jMax -= 1
        iMax -= 1
        iMin += 1
        jMin += 1
    return output