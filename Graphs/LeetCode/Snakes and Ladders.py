# 909, BFS with matrix unpacking | O(N ^ 2) and O(N ^ 2)
from typing import List
from collections import deque


def snakesAndLadders(board: List[List[int]]) -> int:
    n = len(board)
    size = n ** 2
    pos_map = [0]
    for row in range(n - 1, -1, -1):
        pos_map.extend(board[row] if (n - row) % 2 else board[row][::-1])

    queue = deque([1])
    level = 0
    visited = {1}
    while queue:
        level += 1
        for _ in range(len(queue)):
            val = queue.popleft()
            for next_val in range(val + 1, min(val + 6, size) + 1):
                next_val = next_val if pos_map[next_val] == -1 else pos_map[next_val]
                if next_val not in visited:
                    visited.add(next_val)
                    if next_val == size:
                        return level
                    queue.append(next_val)

    return -1
