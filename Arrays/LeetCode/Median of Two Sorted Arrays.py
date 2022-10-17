# 4, Two Pointer | O((N + M)/2) and O(1)
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    p1 = 0
    p2 = 0
    val = len(nums1) + len(nums2)
    if val % 2 == 0:
        mid1, mid2 = val // 2 - 1, val // 2
    else:
        mid1 = mid2 = val // 2
    count = 0
    total = 0
    while p1 < len(nums1) and p2 < len(nums2):
        count += 1
        if nums1[p1] > nums2[p2]:
            num = nums2[p2]
            p2 += 1
        else:
            num = nums1[p1]
            p1 += 1
        if count == mid1 + 1:
            total += num
        if count == mid2 + 1:
            total += num
            break

    if count < mid2 + 1:
        if p1 != len(nums1):
            while count < mid2 + 1:
                num = nums1[p1]
                p1 += 1
                if count == mid1:
                    total += num
                if count == mid2:
                    total += num
                count += 1
        else:
            while count < mid2 + 1:
                num = nums2[p2]
                p2 += 1
                if count == mid1:
                    total += num
                if count == mid2:
                    print(num)
                    total += num
                count += 1

    return total / 2
