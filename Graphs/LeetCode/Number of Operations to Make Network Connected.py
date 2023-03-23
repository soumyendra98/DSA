# 1319, Union Find | O(N * log(N)) and O(N)
from typing import List


def makeConnected(n: int, connections: List[List[int]]) -> int:
    uf = {i: i for i in range(n)}
    rank = {i: 1 for i in range(n)}

    if len(connections) < n - 1:
        return -1

    def find(x):
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            if rank[rx] < rank[ry]:
                uf[rx] = ry
                rank[ry] += rank[rx]
            else:
                uf[ry] = rx
                rank[rx] += rank[ry]

    for x, y in connections:
        union(x, y)

    roots = set()

    for i in range(n):
        roots.add(find(i))

    return len(roots) - 1
