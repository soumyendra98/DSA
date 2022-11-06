# 1024, Maximizing the start (arr[i] + i) | O(N) and O(1)
from typing import List


def maxScoreSightseeingPair(values: List[int]) -> int:
    start = values[0]
    max_score = 0
    for i in range(1, len(values)):
        if start + values[i] - i > max_score:
            max_score = start + values[i] - i
        if values[i] + i > start:
            start = values[i] + i
    return max_score
