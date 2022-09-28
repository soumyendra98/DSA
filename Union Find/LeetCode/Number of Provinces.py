# 547, Simple Union find and Set | O(N ^ 2) and O(N)
from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    union = {x: x for x in range(n)}

    def find(i):
        if i != union[i]:
            union[i] = find(union[i])
        return union[i]

    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1:
                union[find(i)] = find(j)
    find_set = set()
    for i in range(n):
        val = find(i)
        find_set.add(val)

    return len(find_set)
