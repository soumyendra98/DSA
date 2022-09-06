# Implementation of a Doubly Linked List
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) and O(1)
    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    # O(1) and O(1)
    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    # O(1) and O(1)
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            prev = node.prev
            prev.next = nodeToInsert

        node.prev = nodeToInsert

    # O(1) and O(1)
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            next = node.next
            next.prev = nodeToInsert

        node.next = nodeToInsert

    # O(P) and O(1)
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return

        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            if count == position:
                self.insertBefore(curr, nodeToInsert)
                return
            curr = curr.next

        if count == position:
            self.setTail(nodeToInsert)

    # O(N) and O(1)
    def removeNodesWithValue(self, value):
        # Write your code here.
        curr = self.head
        while curr is not None:
            if curr.value == value:
                next = curr.next
                self.remove(curr)
                curr = next
            else:
                curr = curr.next

    # O(1) and O(1)
    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    # O(N) and O(1)
    def containsNodeWithValue(self, value):
        # Write your code here.
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False
