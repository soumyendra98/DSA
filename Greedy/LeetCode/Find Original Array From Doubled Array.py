# 2007, Sorting and Greedy | O(N) and O(N)
from collections import Counter
from typing import List


def findOriginalArray(changed: List[int]) -> List[int]:
    if len(changed) % 2 != 0:
        return []

    changed.sort()

    output = []
    changed_dict = Counter(changed)

    count = len(changed) // 2

    for val in changed:
        if val * 2 in changed_dict and changed_dict[val] > 0:
            changed_dict[val] -= 1
            changed_dict[2 * val] -= 1
            count -= 1
            output.append(val)
        elif changed_dict[val] > 0:
            return []

    if count == 0:
        return output
    else:
        return []
