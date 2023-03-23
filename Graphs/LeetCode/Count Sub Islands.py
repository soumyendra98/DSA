# 1905, DFS | O(N * M) and O(N * M)
from typing import List


def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    M, N = len(grid1), len(grid1[0])

    def dfs(r, c):
        grid2[r][c] = 0
        out = grid1[r][c] == 1
        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= x < M and 0 <= y < N and grid2[x][y]:
                out &= dfs(x, y)
        return out

    count = 0
    for i in range(M):
        for j in range(N):
            if grid2[i][j] == 1:
                if dfs(i, j):
                    count += 1

    return count
