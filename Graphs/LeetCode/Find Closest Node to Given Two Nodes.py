# 2359, BFS | O(N) and O(N)
from typing import List


def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    if node1 == node2:
        return node1

    n = len(edges)
    s1 = {node1}
    s2 = {node2}
    ans = 10 ** 5
    while node1 >= 0 or node2 >= 0:
        if edges[node1] != -1:
            node1 = edges[node1]
        if edges[node2] != -1:
            node2 = edges[node2]
        if node1 in s1 and node2 in s2:
            break
        s1.add(node1)
        s2.add(node2)

        if node1 in s2:
            ans = min(ans, node1)
        if node2 in s1:
            ans = min(ans, node2)
        if ans < 10 ** 5:
            return ans
    return -1
