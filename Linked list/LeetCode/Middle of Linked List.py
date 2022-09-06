# 21 Two Pointer, Floyd Cycle Detection| O(N/2) and O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast is not None:
        if fast.next is not None:
            fast = fast.next.next
        else:
            fast = None
            break
        slow = slow.next
    return slow


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(4, None)

print(middleNode(l1).val)