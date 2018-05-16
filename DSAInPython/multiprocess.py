from multiprocessing import Process, Pipe, Queue, Lock


def square(n, l):
    #l.acquire()
    print "Square of {} is {}".format(n, n*n)
    l.send(n*n)
    #l.release()


n = 5
l = Lock()
p_con, c_con = Pipe()
for i in range(0,6):
    p = Process(target=square,args=(i,c_con))
    p.start()
    p.join()
    print "Pipe", p_con.recv()
