class Node:

    def __init__(self, val):
        self.data = val
        self.next = None

class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0


    def enqueue(self, val):
        temp = Node(val)
        if self.isEmpty():
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
        self.count += 1


    def dequeue(self):
        if self.isEmpty():
            val = None
            #  self.front = self.rear = temp
        else:
            val = self.front.data
            self.front = self.front.next
        self.count -= 1
        return val


    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0


q = MyQueue()
print(q.isEmpty())
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())
print(q.isEmpty())
print(q.size())
