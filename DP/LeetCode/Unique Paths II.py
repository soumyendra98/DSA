# Space Optimized DP | O(N * M) and O(M)
from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    n = len(obstacleGrid)
    m = len(obstacleGrid[0])

    if obstacleGrid[0][0]:
        return 0

    prev = [0 for _ in range(m)]
    curr = [0 for _ in range(m)]
    curr[0] = 1
    for i in range(n):
        for j in range(m):
            if obstacleGrid[i][j] == 0:
                if i == 0:
                    if j - 1 > -1:
                        curr[j] = curr[j - 1]
                elif j == 0:
                    if i - 1 > -1:
                        curr[j] = prev[j]
                else:
                    curr[j] = prev[j] + curr[j - 1]
            else:
                curr[j] = 0
        prev = curr[:]
    return curr[m - 1]
