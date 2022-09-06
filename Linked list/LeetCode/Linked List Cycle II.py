# 142 Two Pointer, Floyd Cycle Detection| O(N) and O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast is not None:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return None
        if slow == fast:
            break
    if fast is None:
        return None
    while head != slow:
        head = head.next
        slow = slow.next

    return head


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(4, None)

print(detectCycle(l1))
