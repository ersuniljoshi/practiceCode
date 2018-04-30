class dqueue(object):

    def __init__(self):
        self.q = []

    def fdqueue(self):
        if len(self.q) > 0:
            return self.q.pop(0)
        else:
            print "Empty Queue"
            return None


    def rdqueue(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            print "Empty Queue"
            return None

    def fenqueue(self, value):
        self.q.insert(0,value)

    def renqueue(self, value):
        self.q.append(value)


    def size(self):
        return len(self.q)

    def isempty(self):
        return len(self.q) == 0


dq = dqueue()
dq.fenqueue(1)
dq.fenqueue(2)
dq.fenqueue(3)
dq.fenqueue(4)
dq.fenqueue(5)
dq.fenqueue(6)
dq.fenqueue(8)
print dq.fdqueue()
print dq.rdqueue()


