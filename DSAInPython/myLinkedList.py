class Node:
    __slots__ = '__data', '__next'

    def __init__(self, value):
        self.__data = value
        self.__next = None

    def getData(self):
        return self.__data

    def setData(self, value):
        self.__data = value

    def getNext(self):
        return self.__next

    def setNext(self, newNext):
        self.__next = newNext


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def addNode(self, value):
        temp = Node(value)
        temp.setNext(self.__head)
        self.__head = temp
        self.__size += 1

    def isEmpty(self):
        return self.__head is None

    def searchElement(self, item):
        pass

    def removeNode(self, item):
        current = self.__head
        while current is not None:
            if current.getData() == item:

    def printLL(self):
        current = self.__head
        while current is not None:
            print "{0}->".format(current.getData()),
            current = current.getNext()

    def size(self):
        return self.__size


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.addNode(5)
    mylist.addNode(5)
    mylist.addNode(4)
    mylist.addNode(9)
    mylist.addNode(0)
    mylist.printLL()
