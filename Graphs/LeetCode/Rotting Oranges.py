# 904, BFS on graphs | O(N) and O(N)
from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    fresh_count = 0
    queue = deque()

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    time = 0
    dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        if fresh_count == 0:
            return time
        for idx in range(len(queue)):
            i, j = queue.popleft()

            for x, y in dr:
                r, c = i + x, j + y
                if m > r >= 0 and n > c >= 0 and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh_count -= 1
                    queue.append((r, c))
        time += 1

    return time if fresh_count == 0 else -1
