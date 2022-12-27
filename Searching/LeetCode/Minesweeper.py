# 529, DFS | O(N * M) and O(N * M)
from collections import defaultdict
from typing import List


def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    directions = [1, 0, -1]
    m = len(board)
    n = len(board[0])
    r_mines = defaultdict(int)
    # cannot_visit = set(['B', 'M'])
    # row, col = click

    # If we click on a mine
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    # Create all places where we need to stop propogation (Process the MINES)
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'M':
                for i in directions:
                    for j in directions:
                        if r + i < 0 or r + i == m or c + j < 0 or c + j == n:
                            continue
                        if not (i == 0 and j == 0):
                            r_mines[(r + i, c + j)] += 1

    # DFS
    def dfs(r, c):
        if r < 0 or r == m or c < 0 or c == n or board[r][c] in ('B', 'M'):
            return
        if (r, c) in r_mines:
            board[r][c] = str(r_mines[(r, c)])
            return

        board[r][c] = 'B'

        for i in directions:
            for j in directions:
                if not (i == 0 and j == 0):
                    dfs(r + i, c + j)

    dfs(click[0], click[1])

    return board
