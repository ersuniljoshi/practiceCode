from threading  import Thread, Lock

def sum(a, b, l):
    l.acquire()
    print(a,b)
    l.release()
a = 5
b = 5
l = Lock()
t1 = Thread(target=sum, args=(a,b,l))
t2 = Thread(target=sum, args=(a,b,l))

t1.start()
t2.start()
t1.join()
t2.join()
