class A:
    def sum(self, *args):
        sum = 0
        for i in args:
            sum += i
        print sum

a = A()
a.sum(1,2,3,4,5, 6, 7,8)