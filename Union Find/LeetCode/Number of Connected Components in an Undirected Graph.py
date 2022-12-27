# 323,
from typing import List


def countComponents(n: int, edges: List[List[int]]) -> int:
    uf = {x: x for x in range(n)}
    rank = {x: 1 for x in range(n)}

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

    for x, y in edges:
        union(x, y)

    roots = set()
    for i in range(n):
        val = find(i)
        roots.add(val)
    return len(roots)
