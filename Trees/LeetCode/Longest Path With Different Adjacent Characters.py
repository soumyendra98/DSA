# 2246, DFS and Diameter of tree | O(N) and O(N)
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


def longestPath(parent: List[int], s: str) -> int:
    n = len(parent)
    tree = defaultdict(list)

    for i in range(n):
        if parent[i] == -1:
            continue
        tree[parent[i]].append(i)
        tree[i].append(parent[i])

    max_len = 0

    def dfs(node, prev):
        temp = []
        for next_node in tree[node]:
            if next_node != prev:
                val = dfs(next_node, node)
                if val:
                    if len(temp) < 2:
                        heappush(temp, val)
                    else:
                        if temp[0] < val:
                            heappop(temp)
                            heappush(temp, val)

        nonlocal max_len
        max_len = max(max_len, 1 + sum(temp))

        if s[node] != s[prev]:
            return 1 + (max(temp) if temp else 0)
        else:
            return 0

    dfs(0, 0)
    return max_len
