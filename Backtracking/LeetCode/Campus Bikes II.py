# 1066, Using Backtracking | O(M!/(M−N)!) and O(N + M)
from typing import List


def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> int:
    visited = {}
    n = len(bikes)
    w = len(workers)

    def manhattanDistance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def backtrack(arr, idx):
        if idx == w:
            return 0

        if (idx, tuple(arr)) in visited:
            return visited[(idx, tuple(arr))]

        temp = float('inf')
        for i in range(n):
            if arr[i] == 0:
                temp = min(temp,
                           manhattanDistance(workers[idx], bikes[i]) + backtrack(arr[:i] + [1] + arr[i + 1:], idx + 1))

        visited[(idx, tuple(arr))] = temp
        return visited[(idx, tuple(arr))]

    return backtrack([0] * n, 0)
