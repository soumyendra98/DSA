# 542, BFS | O(N * M) and O(N * M)
from collections import deque
from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    queue = deque([])
    M, N = len(mat), len(mat[0])

    for i in range(M):
        for j in range(N):
            if not mat[i][j]:
                queue.append((i, j))

    distance = 0
    grid = [[0 for _ in range(N)] for _ in range(M)]

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            grid[r][c] = distance
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < M and 0 <= y < N and mat[x][y] == 1:
                    queue.append((x, y))
                    mat[x][y] = 0

        distance += 1
    return grid
