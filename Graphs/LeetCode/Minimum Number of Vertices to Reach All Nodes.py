# 1557, Indegree | O(N + E) and O(N)
from typing import List


def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    indegree = set()

    for f, t in edges:
        indegree.add(t)

    output = []
    for i in range(n):
        if i not in indegree:
            output.append(i)

    return output
