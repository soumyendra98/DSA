# 733, Recursion and DFS | O(N) and O(N)
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    row = len(image)
    col = len(image[0])
    start = image[sr][sc]

    if start == color:
        return image

    def fill(r, c):
        if r >= row or c >= col or r < 0 or c < 0 or image[r][c] != start:
            return image
        image[r][c] = color

        fill(r, c + 1)
        fill(r, c - 1)
        fill(r + 1, c)
        fill(r - 1, c)

    fill(sr, sc)
    return image
