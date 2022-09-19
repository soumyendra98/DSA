# Sort the Zip on the decreasing efficiency and then form a min heap of speed and calculate
# performance on the entire array | O(N) and O(N + K)

from typing import List
from heapq import heappop, heappush


def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    performances = sorted(zip(efficiency, speed), reverse=True)

    speed_sum, heap, performance = 0, [], 0

    for e, s in performances:
        if len(heap) > k - 1:
            speed_sum -= heappop(heap)

        heappush(heap, s)
        speed_sum += s

        performance = max(performance, speed_sum * e)

    return performance % (10 ** 9 + 7)