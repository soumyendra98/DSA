# 42, DP using Max Left and Max Right |O(N) and O(N)
from typing import List


def trap(height: List[int]) -> int:
    h = len(height)
    dp_left = [0] * h
    dp_right = [0] * h
    max_left = max_right = 0
    water_trap = 0

    for idx in range(h):
        max_left = max(max_left, height[idx])
        max_right = max(max_right, height[h - idx - 1])
        dp_left[idx] = max_left
        dp_right[h - idx - 1] = max_right

    for idx in range(1, h):
        if height[idx] < min(dp_left[idx], dp_right[idx]):
            water_trap += min(dp_left[idx], dp_right[idx]) - height[idx]

    return water_trap
