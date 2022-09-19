# 621, Find max count and check total | O(N) and O(1)
from typing import List
from collections import Counter


def leastInterval(tasks: List[str], n: int) -> int:
    task_count = Counter(tasks)
    max_count = max(task_count.values())

    total = (max_count - 1) * (n + 1)
    for count in task_count.values():
        if count == max_count:
            total += 1

    return max(total, len(tasks))
