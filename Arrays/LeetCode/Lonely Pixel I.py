# 531, Column wise Traversal | O(M * N) and O(1)
from typing import List


def findLonelyPixel(picture: List[List[str]]) -> int:
    m = len(picture)
    n = len(picture[0])
    total = 0
    for col in range(n):
        count = 0
        r = 0
        for row in range(m):
            if picture[row][col] == 'B':
                count += 1
                r = row
            if count > 1:
                break
        if count == 1 and picture[r].count('B') == 1:
            total += 1
    return total
