from typing import List


# If the target exists, returns its leftmost index.
# Else, returns the index of where it should be.
def binarySearchLeft(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l


# If the target exists, returns its rightmost index.
# Else, returns the index of where it should be.
def binarySearchRight(nums: List[int], target: int) -> int:

    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid

    return l