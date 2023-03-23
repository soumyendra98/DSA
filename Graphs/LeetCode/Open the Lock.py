# 752, BFS | O((N ^ 2) * (A ^ N) + D) and O((A ^ N) + D)
from collections import deque
from typing import List


def openLock(deadends: List[str], target: str) -> int:
    deadset = set(deadends)

    if "0000" in deadends:
        return -1

    queue = deque(["0000"])
    visited = {"0000"}
    turns = 0

    def getNext(node):
        for i in range(4):
            x = int(node[i])
            for diff in (1, -1):
                y = (x + diff + 10) % 10
                yield node[:i] + str(y) + node[i + 1:]

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node == target:
                return turns

            for next_node in getNext(node):
                if next_node not in visited and next_node not in deadset:
                    queue.append(next_node)
                    visited.add(next_node)
        turns += 1

    return -1
