# 216,
from typing import List


def validTree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    rank = {x: 1 for x in range(n)}
    uf = {x: x for x in range(n)}

    def find(x):
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)

        if rx != ry:
            if rank[rx] > rank[ry]:
                uf[ry] = rx
            elif rank[rx] < rank[ry]:
                uf[rx] = ry
            else:
                uf[ry] = rx
                rank[rx] += 1
            return True
        else:
            return False

    for x, y in edges:
        if not union(x, y):
            return False

    return True
