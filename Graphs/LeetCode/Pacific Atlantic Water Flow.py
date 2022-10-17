# 417, Using DFS | O(N * M) and  O(N * M)
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    m = len(heights)
    n = len(heights[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    p_set = set()
    a_set = set()

    def dfs(r, c, h, coordinates):
        if r >= m or r < 0 or c >= n or c < 0:
            return
        if (r, c) in coordinates:
            return
        if heights[r][c] < h:
            return
        coordinates.add((r, c))
        for i, j in directions:
            dfs(r + i, c + j, heights[r][c], coordinates)

    for i in range(m):
        dfs(i, 0, 0, p_set)
        dfs(i, n - 1, 0, a_set)
    for j in range(n):
        dfs(0, j, 0, p_set)
        dfs(m - 1, j, 0, a_set)
    return list(p_set & a_set)

