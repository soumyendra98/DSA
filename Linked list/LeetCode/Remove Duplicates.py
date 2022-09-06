# 83, Simple Iteration | O(N) and O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    curr = head
    while curr.next is not None:
        if curr.val == curr.next.val:
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None
        else:
            curr = curr.next

    return head


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(4, None)

print(deleteDuplicates(l1))