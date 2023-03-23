# 934,
from collections import deque
from typing import List


def shortestBridge(grid: List[List[int]]) -> int:
    queue1 = deque([])
    queue2 = deque([])
    N = len(grid)

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                queue1.append((i, j))
                break
        if queue1:
            break

    while queue1:
        r, c = queue1.popleft()
        if grid[r][c] == 0:
            queue2.append((r, c))
            continue
        if grid[r][c] == 1:
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < N and 0 <= y < N and grid[x][y] != -1:
                    queue1.append((x, y))
        grid[r][c] = -1

    flips = 0

    while queue2:
        for _ in range(len(queue2)):
            r, c = queue2.popleft()
            if grid[r][c] == 1:
                return flips
            if grid[r][c] == 0:
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < N and 0 <= y < N and grid[x][y] != -1:
                        queue2.append((x, y))
            grid[r][c] = -1
        flips += 1
