from pythonds.basic.stack import Stack


class MyQueue:

    def __init__(self):
        self.ens1 = Stack()
        self.des2 = Stack()

    def enqueue(self, value):
        self.ens1.push(value)

    def dequeue(self):
        if self.ens1.size() == 0 and self.des2.size() == 0:
            return "Queue Is Empty"

        if self.des2.isEmpty():
            while not self.ens1.isEmpty():
                self.des2.push(self.ens1.pop())
        return self.des2.pop()

    def size(self):
        return self.ens1.size() + self.des2.size()


q = MyQueue()
q.enqueue(15)
q.enqueue(5)
q.enqueue(6)
q.enqueue(16)
q.enqueue(26)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()




