# 378, Using Binary Search | O(N * log(max - min) and O(1)
from typing import List
from bisect import bisect


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]

    while low < high:
        mid = (low + high) // 2
        count = 0
        for i in range(n):
            count += bisect(matrix[i], mid)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low
