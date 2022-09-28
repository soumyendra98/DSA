# 57, Using Greedy | O(N) and O(N)
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
        return [newInterval]

    output = []

    for val in intervals:
        if newInterval is None or newInterval[0] > val[1]:
            output.append(val)
        elif newInterval[1] < val[0]:
            output.append(newInterval)
            output.append(val)
            newInterval = None
        else:
            newInterval[0] = min(newInterval[0], val[0])
            newInterval[1] = max(newInterval[1], val[1])

    if newInterval is not None:
        output.append(newInterval)
    return output
