# 1926, Simple BFS | O(M * N) and O(max(M, N))
from collections import deque
from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    m = len(maze)
    n = len(maze[0])
    queue = deque([(*entrance, 0)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    while queue:
        length = len(queue)
        while length > 0:
            i, j, count = queue.popleft()
            if [i, j] != entrance and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                return count
            for x, y in directions:
                if 0 <= i + x < m and 0 <= j + y < n and (i + x, j + y) not in visited and maze[i + x][j + y] != '+':
                    visited.add((i + x, j + y))
                    queue.append((i + x, j + y, count + 1))
            length -= 1

    return -1
