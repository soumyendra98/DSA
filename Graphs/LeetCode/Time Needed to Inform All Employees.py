# 1376, BFS | O(N) and O(N)
from collections import deque, defaultdict
from typing import List


def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    tree = defaultdict(list)

    for i in range(n):
        tree[manager[i]].append(i)

    queue = deque([(headID, 0)])
    time = 0
    while queue:
        node, t = queue.popleft()
        for next_node in tree[node]:
            queue.append((next_node, t + informTime[node]))
        if informTime[node] == 0:
            time = max(time, t)
    return time
