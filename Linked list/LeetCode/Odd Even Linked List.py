# 328, Linked List Traversal | O(N) and O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    if head.next is None or head.next.next is None:
        return head

    odd_head = head
    even_head = head.next
    temp = head.next

    while odd_head.next is not None and even_head.next is not None:

        if odd_head.next is not None and odd_head.next.next is not None:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
        else:
            odd_head.next = None

        if even_head.next is not None and even_head.next.next is not None:
            even_head.next = even_head.next.next
            even_head = even_head.next
        else:
            even_head.next = None

    odd_head.next = temp

    return head

