# 149, Slope of a line | O(N ^ 2) and O(N)
from collections import defaultdict
from typing import List


def maxPoints(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 1:
        return n

    output = 0

    for i in range(n - 1):
        slope_map = defaultdict(int)
        for j in range(i + 1, n):
            if points[i][0] == points[j][0]:
                slope_map[float('inf')] += 1
            else:
                slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                slope_map[slope] += 1
        output = max(output, max(slope_map.values()))
    return output + 1
