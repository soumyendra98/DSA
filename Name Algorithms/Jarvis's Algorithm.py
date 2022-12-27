# 587, Using Jarvis Algorithm | O(M * N) and O(M)
from typing import List


def outerTrees(trees: List[List[int]]) -> List[List[int]]:
    n = len(trees)
    trees.sort(key=lambda x: (x[0], -x[1]))

    if n < 3:
        return trees

    def orientation(p, q, r):
        # (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)
        val = (q[1] - p[1]) * (r[0] - q[0]) - ((r[1] - q[1]) * (q[0] - p[0]))

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    p = 0
    q = 0
    hull = set()
    idx = 0
    while True:
        hull.add(tuple(trees[p]))
        q = (p + 1) % n
        for i in range(n):
            if orientation(trees[p], trees[i], trees[q]) == 2:
                q = i
        for i in range(n):
            if i != p and i != q and orientation(trees[p], trees[i], trees[q]) == 0:
                hull.add(tuple(trees[i]))
        p = q
        if p == 0:
            break
        idx += 1
    return hull
