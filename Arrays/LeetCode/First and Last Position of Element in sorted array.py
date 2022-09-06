# 34, Binary Search | O(N) and O(1)
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    output = [-1, -1]
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            output[0] = mid
            right = mid - 1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            output[1] = mid
            left = mid + 1

    return output


arr = [5, 7, 7, 8, 8, 10]

print(searchRange(arr, 8))
