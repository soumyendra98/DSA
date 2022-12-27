# 84, Monotonic Stack | O(N) and O(N)
from collections import deque
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    max_area = 0
    stack = deque([])
    for i in range(n):
        idx = -1
        while stack and stack[-1][0] > heights[i]:
            val, idx = stack.pop()
            max_area = max(max_area, val * (i - idx))
        if idx != -1:
            stack.append((heights[i], idx))
        else:
            stack.append((heights[i], i))
    while stack:
        val = stack.pop()
        max_area = max(max_area, val[0] * (n - val[1]))
    return max_area
