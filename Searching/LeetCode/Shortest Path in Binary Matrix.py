# 1091, BFS | O(N ^ 2) and O(log(N ^ 2))
from typing import List
from collections import deque


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] or grid[-1][-1]:
        return -1
    n = len(grid)
    queue = deque([(0, 0, 1)])
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    grid[0][0] = -1

    while queue:
        r, c, length = queue.popleft()

        if r == n - 1 and c == n - 1:
            return length

        for i, j in directions:
            x, y = r + i, c + j
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                queue.append((x, y, length + 1))
                grid[x][y] = -1

    return -1
