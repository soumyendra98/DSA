# 2316, Count Unreachable Pairs of Nodes in an Undirected Graph | O(N) and O(N)
from typing import List
from collections import Counter
def countPairs(n: int, edges: List[List[int]]) -> int:
    root = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find(x):
        if x != root[x]:
            root[x] = find(root[x])
        return root[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)

        if rx != ry:
            if rank[rx] < rank[ry]:
                root[rx] = ry
                rank[ry] += rank[rx]
            else:
                root[ry] = rx
                rank[rx] += rank[ry]

    for x, y in edges:
        union(x, y)

    total = 0
    unique = Counter([find(i) for i in range(n)])
    counts = list(unique.values())
    start = counts[0]
    for i in range(1, len(counts)):
        total += start * counts[i]
        start += counts[i]
    return total