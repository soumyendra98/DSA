# 1201, Sorting and UF | O(N) and O(N)
from collections import defaultdict
from typing import List


def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
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

    for x, y in pairs:
        union(x, y)

    sub_strings = defaultdict(list)

    for i in range(n):
        sub_strings[find(i)].append(s[i])

    for key, value in sub_strings.items():
        sub_strings[key] = sorted(value, reverse=True)

    temp = []

    for i in range(n):
        temp.append(sub_strings[uf[i]].pop())

    return "".join(temp)
