# 2095, Floyd's Cycle detection | O(N) and O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        return None
    prev = None
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head
