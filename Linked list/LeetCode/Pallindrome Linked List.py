#Reverse a linked List |O(N) and O(N)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    if head.next is None:
        return True
    arr = []
    count = 0
    curr, prev = head, None
    while curr is not None:
        arr.append(curr.val)
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count += 1

    for i in range(count // 2):
        if arr[i] != prev.val:
            return False
        prev = prev.next

    return True

