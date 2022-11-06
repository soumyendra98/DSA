# 2136, Plant Faster Growing First | O(NlogN) and O(N)
from typing import List


def earliestFullBloom(plantTime: List[int], growTime: List[int]) -> int:
    sorted_seeds = sorted(zip(plantTime, growTime), key=lambda x: x[1])
    total_time = 0
    for pt, gt in sorted_seeds:
        total_time = pt + max(total_time, gt)

    return total_time

