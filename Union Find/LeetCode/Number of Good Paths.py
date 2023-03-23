# 2421, Union Find with Rank | O(N * Log(N)) and O(N)
from typing import List


def numberOfGoodPaths(vals: List[int], edges: List[List[int]]) -> int:
    n = len(vals)
    uf = [i for i in range(n)]
    rank = [1] * n

    def find(x):
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        val = 0
        if vals[rx] == vals[ry]:
            uf[ry] = rx
            val = rank[rx] * rank[ry]
            rank[rx] += rank[ry]
        elif vals[rx] > vals[ry]:
            uf[ry] = rx
        else:
            uf[rx] = ry
        return val

    edges = sorted(edges, key=lambda x: max(vals[x[0]], vals[x[1]]))
    total = n
    for x, y in edges:
        total += union(x, y)

    return total
