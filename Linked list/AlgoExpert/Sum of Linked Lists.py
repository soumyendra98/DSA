# Two Pointer | O(N+M) and O(N+M)
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    p1 = linkedListOne
    p2 = linkedListTwo
    linkedListThree = LinkedList(0)
    head = linkedListThree
    carry = 0
    while p1 or p2:
        sum = carry
        if p1:
            sum += p1.value
        if p2:
            sum += p2.value
        carry = (sum - (sum % 10)) // 10
        linkedListThree.value = sum % 10

        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
        if p1 or p2 or carry != 0:
            linkedListThree.next = LinkedList(carry)
            linkedListThree = linkedListThree.next

    return head
