# 1272, Number Theory | O(N) and O(N)
from typing import List


def removeInterval(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    output = []
    start, end = toBeRemoved[0], toBeRemoved[1]

    for val in intervals:
        if val[1] <= start or val[0] >= end:
            output.append(val)
        elif val[0] < start and val[1] <= end:
            output.append([val[0], start])
        elif val[0] > start and val[1] > end:
            output.append([end, val[1]])
        elif val[0] <= start and end <= val[1]:
            if val[0] != start:
                output.append([val[0], start])
            if val[1] != end:
                output.append([end, val[1]])

    return output
