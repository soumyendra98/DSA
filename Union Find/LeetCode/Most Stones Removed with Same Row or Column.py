# 947, Using Union Find | O(N) and O(N)
from typing import List


def removeStones(stones: List[List[int]]) -> int:
    if len(stones) == 1:
        return 0

    output = len(stones)
    union = {}

    def find(i):
        if i != union.setdefault(i, i):
            union[i] = find(union[i])
        return union[i]

    for i, j in stones:
        union[find(i)] = find(~j)

    uf = {find(x) for x in union}
    output -= len(uf)
    return output
