# Sorting and two pointer | O(NlogN) and O(N)
from collections import defaultdict


def taskAssignment(k, tasks):
    # Write your code here.
    indices_map = defaultdict(list)
    for idx, val in enumerate(tasks):
        indices_map[val].append(idx)
    tasks.sort()
    output = []
    left, right = 0, 2 * k - 1
    while left < right:
        output.append([indices_map[tasks[left]].pop(), indices_map[tasks[right]].pop()])
        right -= 1
        left += 1
    return output
