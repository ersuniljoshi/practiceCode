from pythonds.basic.queue import Queue
from pythonds.basic.stack import Stack


def reverseKElement(myQ, count):
    st = Stack()
    qlen = len(myQ.items)
    # print qlen
    for i in range(0,count):
        st.push(myQ.dequeue())
    # print myQ.items
    while not st.isEmpty():
        myQ.enqueue(st.pop())
    # print myQ.items
    for i in range(0, qlen-count):
        myQ.enqueue(myQ.dequeue())

    return myQ.items


q = Queue()
k = 9
for i in range(20,0,-1):
    q.enqueue(i)
# print(q.dequeue())

print("Before", q.items)
print("After", reverseKElement(q, k))
