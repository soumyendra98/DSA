# DFS | O(N*M) and O(N*M)
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    row = len(grid)
    col = len(grid[0])
    count = 0

    def dfs(r, c):
        if r >= row or c >= col or r < 0 or c < 0 or grid[r][c] == '0':
            return

        grid[r][c] = '0'

        dfs(r, c + 1)
        dfs(r, c - 1)
        dfs(r + 1, c)
        dfs(r - 1, c)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count

