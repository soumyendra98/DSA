# 56, Sorting and Merge | O(NlogN) and O(N)
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    curr = intervals[0]
    output = [curr]

    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]

        if curr[0] <= start <= curr[1] or curr[0] <= end <= curr[1]:
            curr[0], curr[1] = curr[0], max(curr[1], end)
        else:
            curr = [start, end]
            output.append(curr)

    return output
