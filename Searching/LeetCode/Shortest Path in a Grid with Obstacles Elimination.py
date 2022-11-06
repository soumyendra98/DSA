# 1293, BFS | O(N * M * K) and O(N * M * K)
from collections import deque
from typing import List


def shortestPath(grid: List[List[int]], k: int) -> int:
    n = len(grid)
    m = len(grid[0])
    if k > n - 1 + m - 1:
        return n - 1 + m - 1

    queue = deque([[0, 0, k, 0]])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    visited = set([(0, 0, k)])

    while queue:
        r, c, ele, steps = queue.popleft()

        if r == n - 1 and c == m - 1:
            return steps

        for i, j in directions:
            ri, cj = r + i, c + j
            if -1 < ri < n and -1 < cj < m and grid[ri][cj] <= ele and (ri, cj, ele - grid[ri][cj]) not in visited:
                visited.add((ri, cj, ele - grid[ri][cj]))
                queue.append([ri, cj, ele - grid[ri][cj], steps + 1])

    return -1
