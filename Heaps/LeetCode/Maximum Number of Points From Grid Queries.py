# 2503, Heap and Binary Search | O(N * M + Q * log(N * M)) O(N * M)
from heapq import heappop, heappush
from bisect import bisect
from typing import List
from collections import defaultdict


def maxPoints(grid: List[List[int]], queries: List[int]) -> List[int]:
    m = len(grid)
    n = len(grid[0])

    # BFS
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    loc = defaultdict(lambda: float('inf'))
    res = []
    loc[(0, 0)] = grid[0][0] + 1
    queue = [(grid[0][0] + 1, 0, 0)]

    while queue:
        val, r, c = heappop(queue)
        res.append(val)
        for i, j in directions:
            x = r + i
            y = c + j
            if 0 <= x < m and 0 <= y < n and max(val, grid[x][y] + 1) < loc[(x, y)]:
                heappush(queue, (max(val, grid[x][y] + 1), x, y))
                loc[(x, y)] = max(val, grid[x][y] + 1)
    output = []

    for q in queries:
        output.append(bisect(res, q))

    return output
