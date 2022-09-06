# Simple Iteration | O(N) and O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    curr = linkedList
    while curr.next is not None:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return linkedList


l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(2)
l1.next.next.next = LinkedList(4)

print(removeDuplicatesFromLinkedList(l1))
