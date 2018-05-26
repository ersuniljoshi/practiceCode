from pythonds.basic.queue import Queue
from pythonds.basic.stack import Stack

myQ = Queue()
myQ.enqueue(5)
myQ.enqueue(6)
myQ.enqueue(7)
myQ.enqueue(8)
myQ.enqueue(9)
myQ.enqueue(0)
myQ.enqueue(-5)

def reverseQ(q):
    st = Stack()
    while not q.isEmpty():
        st.push(q.dequeue())

    while not st.isEmpty():
        q.enqueue(st.pop())

    return q.items

print("Before Reverse", myQ.items)
print("After Reverse", reverseQ(myQ))
