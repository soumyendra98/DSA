# 206, Reverse a linked list (similar to swapping) | O(N) and O(N)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(4, None)

print(reverseList(l1))
