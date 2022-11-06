# 296, Use median | O(M * N + Mlog(M) + Nlog(N)) and O(M + N)
from typing import List


def minTotalDistance(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    friends_x = []
    friends_y = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                friends_x.append(i)
                friends_y.append(j)

    friends_x.sort()
    friends_y.sort()
    l = len(friends_x)
    if l % 2 != 0:
        median_x = friends_x[l // 2]
        median_y = friends_y[l // 2]
    else:
        mid = l // 2
        px1, px2 = friends_x[mid - 1: mid + 1]
        py1, py2 = friends_y[mid - 1: mid + 1]
        median_x = (px1 + px2) // 2
        median_y = (py1 + py2) // 2

    dist = 0
    for idx in range(l):
        dist += abs(friends_x[idx] - median_x) + abs(friends_y[idx] - median_y)
    return dist

