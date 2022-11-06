# 23, Min Heap | O(N) and O(N) where N is the total no of nodes across all the lists.
from heapq import heappush, heappop
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for node in lists:
        while node:
            heappush(heap, node.val)
            node = node.next
    if not heap:
        return None

    head = ListNode(heappop(heap))
    curr = head
    while heap:
        curr.next = ListNode(heappop(heap))
        curr = curr.next

    return head
