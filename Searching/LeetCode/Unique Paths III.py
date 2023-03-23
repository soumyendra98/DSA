# 980, DFS + Backtracking | O(3 ^ N) and O(N)
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        self.count = 0
        num_empty = 0
        row = col = -1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    num_empty += 1
                elif grid[i][j] == 1:
                    row, col = i, j

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if len(visited) == num_empty + 1:
                    self.count += 1
                else:
                    return

            visited.add((r, c))
            for i, j in directions:
                if (r + i, c + j) not in visited:
                    dfs(r + i, j + c)
            visited.remove((r, c))

        dfs(row, col)
        return self.count
