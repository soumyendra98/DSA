# 1306, BFS | O(N) and O(N)
from collections import deque
from typing import List


def canReach(arr: List[int], start: int) -> bool:
    n = len(arr)
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()

        if arr[node] == 0:
            return True

        if node + arr[node] < n and (node + arr[node]) not in visited:
            visited.add(node + arr[node])
            queue.append(node + arr[node])

        if node - arr[node] >= 0 and (node - arr[node]) not in visited:
            visited.add(node - arr[node])
            queue.append(node - arr[node])
    return False
