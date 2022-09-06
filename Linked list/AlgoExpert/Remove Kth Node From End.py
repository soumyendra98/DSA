# List Traversal | O(N) and O(1)
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    curr = head
    count = 0
    while curr.next is not None:
        count += 1
        curr = curr.next

    if count == 0:
        head = None

    count -= k

    for index in range(count):
        head = head.next

    if head.next.next is not None:
        if count == -1:
            head.value = head.next.value
        head.next = head.next.next

    else:
        head.next = None


l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)
l1.next.next.next = LinkedList(4)

removeKthNodeFromEnd(l1, 4)
print(l1.value)
