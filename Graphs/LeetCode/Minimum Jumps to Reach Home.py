# 1654, BFS | O(x + max(forbidden) + a + b) and O(x + max(forbidden) + a + b)
from typing import List
from collections import deque


def minimumJumps(forbidden: List[int], a: int, b: int, x: int) -> int:
    max_forbidden = 0
    visited = {(0, 0), (0, 1)}
    for val in forbidden:
        visited.add((val, 0))
        visited.add((val, 1))
        if val > max_forbidden:
            max_forbidden = val

    max_val = x + max_forbidden + a + b

    queue = deque([(0, 0), (0, 1)])
    jumps = 0
    while queue:
        for _ in range(len(queue)):
            node, back = queue.popleft()
            if node == x:
                return jumps

            if node + a <= max_val and (node + a, 1) not in visited:
                queue.append((node + a, 1))
                visited.add((node + a, 1))

            if back and node - b > 0 and (node - b, 0) not in visited:
                queue.append((node - b, 0))
                visited.add((node - b, 0))
        jumps += 1

    return -1
