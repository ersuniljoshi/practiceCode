from pythonds.basic.queue import Queue


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q1.enqueue(val)

    def pop(self):
        if self.len() == 0:
            print("Stack is empty")
            return
        if self.q2.isEmpty():
            while self.q1.size() != 1:
                self.q2.enqueue(self.q1.dequeue())
            self.q1, self.q2 = self.q2, self.q1
        return self.q2.dequeue()

    def len(self):
        return self.q1.size() + self.q2.size()

    def isempty(self):
        return self.len() == 0


s = MyStack()
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(10)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
