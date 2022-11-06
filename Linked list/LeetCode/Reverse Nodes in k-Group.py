# 25, Reversing a linked list | O(N) and O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    reversals = length // k

    def reverse(node):
        prev = None
        curr = node
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev, curr

    curr = head
    head, next = reverse(head)

    for _ in range(reversals - 1):
        start = next
        curr.next, next = reverse(next)
        curr = start

    curr.next = next

    return head
