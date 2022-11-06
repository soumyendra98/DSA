# 376, Hills and Trough | O(N) and O(1)
from typing import List


def wiggleMaxLength(nums: List[int]) -> int:
    n = len(nums)

    if n < 3:
        if len(set(nums)) == n:
            return n
        else:
            return 1

    direction = None
    count = 1
    for i in range(1, n):
        if direction is None:
            if nums[i] > nums[i - 1]:
                direction = True
            elif nums[i] < nums[i - 1]:
                direction = False
        if nums[i] > nums[i - 1] and direction:
            count += 1
            direction = False
        elif nums[i] < nums[i - 1] and not direction:
            count += 1
            direction = True

    return count
