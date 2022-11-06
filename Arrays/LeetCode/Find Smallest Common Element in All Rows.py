# 1198, Frequency calculation | O(N * M) and O(N * M)
from typing import List
from collections import defaultdict


def smallestCommonElement(mat: List[List[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    freq_map = defaultdict(lambda: 0)
    for i in range(m):
        for j in range(n):
            if freq_map[mat[i][j]] == m - 1:
                return mat[i][j]
            freq_map[mat[i][j]] += 1
    # min_val = float('inf')
    # for key, val in freq_map.items():
    #     if val == m and key < min_val:
    #         min_val = key
    # return min_val if min_val != float('inf') else -1
    return -1
