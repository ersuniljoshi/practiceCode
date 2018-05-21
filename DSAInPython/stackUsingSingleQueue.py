from pythonds.basic.queue import Queue


class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, value):
        self.q.enqueue(value)
        length = self.len() - 1
        while length > 0:
            self.q.enqueue(self.q.dequeue())
            length -= 1

    def pop(self):
        return self.q.dequeue() if not self.isEmpty() else "None"

    def len(self):
        return self.q.size()

    def isEmpty(self):
        return self.len() == 0


s = MyStack()
s.push(2)
s.push(3)
s.push(4)
print ( s.pop() )
print ( s.pop() )
print ( s.pop() )
s.push(9)
print ( s.pop() )
print ( s.pop() )
print ( s.pop() )
print ( s.isEmpty() )
