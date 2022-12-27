# 1101, Sorting and UF | O(N + M Log(M)) and O(N + M)
from typing import List


def earliestAcq(logs: List[List[int]], n: int) -> int:
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
            if rank[rx] >= rank[ry]:
                uf[ry] = rx
                rank[rx] += rank[ry]
                return rank[rx]
            else:
                uf[rx] = ry
                rank[ry] += rank[rx]
                return rank[ry]
        return rank[rx]

    logs.sort(key=lambda x: x[0])
    for timestamp, x, y in logs:
        if union(x, y) == n:
            return timestamp

    return -1
