# 695, Using UF | O((N * M) * log(N * M)) and O(N * M)
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, m, n) -> None:
        self.uf = {(i, j): (i, j) for i in range(m) for j in range(n)}

    def find(self, r, c):
        if self.uf[(r, c)] != (r, c):
            self.uf[(r, c)] = self.find(*self.uf[(r, c)])
        return self.uf[(r, c)]

    def union(self, i, j, r, c):
        rx = self.find(i, j)
        ry = self.find(r, c)
        self.uf[ry] = rx


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    uf = UF(M, N)

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < M and 0 <= y < N and grid[x][y] == 1:
                        uf.union(i, j, x, y)
    roots = defaultdict(int)
    max_area = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                roots[uf.find(i, j)] += 1
                max_area = max(roots[uf.find(i, j)], max_area)
    return max_area
