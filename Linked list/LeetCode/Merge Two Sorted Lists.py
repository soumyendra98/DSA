# 21 Merge 2 linked lists | O(M + N) and O(M + N)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    output = ListNode()
    tail = output

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return output.next


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(4, None)

l2 = ListNode(1, None)
l2.next = ListNode(3, None)
l2.next.next = ListNode(4, None)

print(mergeTwoLists(l1, l2).val)
