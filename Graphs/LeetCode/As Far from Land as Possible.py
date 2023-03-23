# 1162, BFS | O(N ^ 2) and O(N ^ 2)
from collections import deque
from typing import List


def maxDistance(grid: List[List[int]]) -> int:
    N = len(grid)
    queue = deque([])
    distance = 0

    self.max_dis = -1

    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                queue.append((r, c))

    while queue:
        level = len(queue)
        while level:
            i, j = queue.popleft()
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < N and 0 <= y < N and grid[x][y] == 0:
                    queue.append((x, y))
                    grid[x][y] = 1
            level -= 1

        if queue:
            distance += 1

    return distance or -1
