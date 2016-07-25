class Queue(object):
    def __init__(self):
        self.items = []

    def Nqueue(self, data):
        self.items.insert(0, data)

    def Dqueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items
