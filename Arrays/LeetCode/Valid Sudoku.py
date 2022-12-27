# 36, Simple Matrix Traversal | O(1) and O(1)
from typing import List
from collections import defaultdict


def isValidSudoku(board: List[List[str]]) -> bool:
    n = len(board)
    col_map = defaultdict(lambda: set())
    row_map = defaultdict(lambda: set())

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                continue
            if board[i][j] in row_map[i] or board[i][j] in col_map[j]:
                return False
            row_map[i].add(board[i][j])
            col_map[j].add(board[i][j])

    for i in range(0, n, 3):
        for j in range(0, n, 3):
            nums_map = set()
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if board[k][l] == '.':
                        continue
                    if board[k][l] in nums_map:
                        return False
                    nums_map.add(board[k][l])
    return True
