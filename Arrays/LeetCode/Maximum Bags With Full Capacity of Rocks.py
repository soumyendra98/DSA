# 2279, Sorting | O(N * Log(N)) and O(N)
from typing import List


def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    empty = [c - r for c, r in zip(capacity, rocks)]
    empty.sort()

    count = 0
    for idx in range(len(empty)):
        if additionalRocks >= empty[idx]:
            count += 1
            additionalRocks -= empty[idx]
        else:
            break
        idx += 1

    return count
