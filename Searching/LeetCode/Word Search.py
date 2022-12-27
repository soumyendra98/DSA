# 79, Simple DFS | O((N * M) ^ 2) and O(N * M)
# Implement Pruning method as well
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    row = len(board)
    col = len(board[0])
    n = len(word)

    def dfs(r, c, widx, visited):
        if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited or word[widx] != board[r][c]:
            return False

        if widx == n - 1 and board[r][c] == word[widx]:
            return True

        visited.add((r, c))
        widx += 1

        val = dfs(r + 1, c, widx, visited)
        val |= dfs(r, c - 1, widx, visited)
        val |= dfs(r - 1, c, widx, visited)
        val |= dfs(r, c + 1, widx, visited)

        visited.remove((r, c))
        return val

    for i in range(row):
        for j in range(col):
            if dfs(i, j, 0, set()):
                return True
    return False
