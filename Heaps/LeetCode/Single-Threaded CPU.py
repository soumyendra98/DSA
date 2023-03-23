# 1834, Heap | O(N * Log(N)) and O(N)
from heapq import heappush, heappop
from typing import List


def getOrder(tasks: List[List[int]]) -> List[int]:
    n = len(tasks)
    for idx, task in enumerate(tasks):
        task.append(idx)

    tasks.sort()

    heap = [(tasks[0][1], tasks[0][2], tasks[0][0])]
    time = tasks[0][0]
    output = []
    idx = 1

    while heap:
        processingTime, index, enqueueTime = heappop(heap)
        time += processingTime
        output.append(index)

        while idx != n and tasks[idx][0] <= time:
            heappush(heap, (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
            idx += 1

        if not heap and idx != n:
            time = tasks[idx][0]
            heappush(heap, (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
            idx += 1

    return output
