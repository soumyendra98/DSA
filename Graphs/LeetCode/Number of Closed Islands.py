# 1254, DFS | O(N * M) and O(N * M)
from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])

    def dfs(r, c):
        if r in (0, M - 1) or c in (0, N - 1):
            return False

        grid[r][c] = -1
        out = True
        for x, y in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if 0 <= x < M and 0 <= y < N and ~grid[x][y]:
                out &= dfs(x, y)
        return out

    count = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:
                if dfs(i, j):
                    count += 1
    return count
