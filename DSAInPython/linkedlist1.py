class Node:

    __slots__ = '_value', '_next'
    def __init__(self, value):
        self._value = value
        self._next = None


class LinkedList:

    __slots__ = '_head', '_size'

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addNodeAtHead(self, value):
        if self.isempty():
            self._head = Node(value)
        else:
            temp = Node(value)
            temp._next = self._head
            self._head = temp
        self._size += 1

    def removeNode(self, value):
        if self.isempty():
           print "Linkedlist is empty"
           return False
        else:
            current = self._head
            previous = None
            while current:
                if current._value == value:
                    break
                previous = current
                current = current._next
            return False

    def getMiddleOfLinkedList(self):
        slowptr = self._head
        fastptr = self._head

        while fastptr is not None and fastptr._next is not None:
            slowptr = slowptr._next
            fastptr = fastptr._next._next

        return slowptr._value

    def getNthOfLinkedList(self, index):
        cur = self._head
        count = 0
        while cur:
            if count == index:
                return cur._value
            count +=1
            cur = cur._next
        return False

    def searchNode(self,value):
        current = self._head
        while current:
            if current._value == value:
                return True
            current = current._next
        return False

    def __str__(self):
        current = self._head
        list = ""
        while current:
            list += str(current._value) +  "->"
            current = current._next
        return list

l = LinkedList()
l.addNodeAtHead(5)
l.addNodeAtHead(6)
l.addNodeAtHead(0)
l.addNodeAtHead(100)
l.addNodeAtHead(101)
l.addNodeAtHead(1)
l.addNodeAtHead(0)
l.addNodeAtHead(10)
l.addNodeAtHead(19)
# l.addNodeAtHead(25)
l.addNodeAtHead(30)

print l
print "Nth", l.getNthOfLinkedList(8)
print "Middle", l.getMiddleOfLinkedList()
# l.removeNode(6)
# print l.searchNode(16)
# print "After", l
