# 399, UF with rank and weights | O(N * Log(N)) and O(N)
from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    n = len(equations)
    uf = {}
    ratio = {}
    rank = {}

    def find(x):
        uf.setdefault(x, x)
        if uf[x] != x:
            prev = uf[x]
            uf[x] = find(uf[x])
            ratio[x] *= ratio[prev] / ratio[uf[x]]
        return uf[x]

    def union(x, y, val):
        rx = find(x)
        ry = find(y)

        if rank[rx] < rank[ry]:
            uf[rx] = ry
            rank[ry] += rank[rx]
            ratio[rx] = ratio[y] * val / ratio[x]
        else:
            uf[ry] = rx
            rank[rx] += rank[ry]
            ratio[ry] = ratio[x] / val / ratio[y]

    for (i, j), val in zip(equations, values):
        if i not in ratio:
            ratio[i] = 1.0
            uf[i] = i
            rank[i] = 1

        if j not in ratio:
            ratio[j] = 1.0
            uf[j] = j
            rank[j] = 1

        union(i, j, val)

    output = []
    for a, b in queries:
        if a in uf and b in uf:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                output.append(ratio[a] / ratio[b])
            else:
                output.append(-1)
        else:
            output.append(-1)

    return output
