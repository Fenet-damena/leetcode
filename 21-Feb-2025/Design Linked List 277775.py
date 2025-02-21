# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        head = self.dummy.next
        temp = head
        counter = 0

        while temp and counter < index:
            temp = temp.next
            counter += 1
        
        if counter == index and temp:
            return temp.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        itr = self.dummy
        
        while itr.next:
            itr = itr.next

        itr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        new_node = Node(val)

        itr = self.dummy
        counter = 0
        while itr and counter < index:
            itr = itr.next
            counter += 1
        
        if counter != index:
            return

        new_node.next = itr.next if itr else None
        if itr:
            itr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        itr = self.dummy
        counter = 0
        while itr and counter < index:
            itr = itr.next
            counter += 1
        
        if counter != index or itr is None or itr.next is None:
            return
        
        itr.next = itr.next.next