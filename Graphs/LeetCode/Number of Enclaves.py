# 1020, DFS | O(N * M) and O(N * M)
from typing import List


def numEnclaves(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    island_size = 0

    def dfs(r, c):
        if r in (0, M - 1) or c in (0, N - 1):
            return False
        grid[r][c] = 2
        nonlocal island_size
        island_size += 1
        out = True
        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= x < M and 0 <= y < N and grid[x][y] == 1:
                out &= dfs(x, y)
        return out

    count = 0

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                if dfs(i, j):
                    count += island_size
                island_size = 0
    return count
