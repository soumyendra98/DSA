# 452, Sorting | O(N * log(N)) and O(1)
from typing import List
def findMinArrowShots(points: List[List[int]]) -> int:
    points = sorted(points, key=lambda x: x[1])

    output = 0
    max_val = -float("inf")

    for start, end in points:
        if start > max_val:
            output += 1
            max_val = end
    return output
