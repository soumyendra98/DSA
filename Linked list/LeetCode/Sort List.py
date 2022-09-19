# 148, Using Merge Sort | O(NlogN) and O(logN)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    def findMid(node):
        slow, fast = node, node

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sort(node):
        if node is None or node.next is None:
            return node

        mid = findMid(node)
        mid_next = mid.next

        mid.next = None

        left = sort(node)
        right = sort(mid_next)
        return mergeSorted(left, right)

    def mergeSorted(left, right):

        if left is None:
            return right

        if right is None:
            return left

        res = None

        if left.val < right.val:
            res = left
            res.next = mergeSorted(left.next, right)
        else:
            res = right
            res.next = mergeSorted(left, right.next)

        return res

    return sort(head)