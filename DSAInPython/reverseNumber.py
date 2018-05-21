from pythonds.basic.stack import Stack


def reverseNumber(num):
    s = Stack()
    while num:
        s.push(num % 10)
        num = num // 10
        # print s

    rev = ""
    while s.size() > 0:
        # print s.size
        rev = str(s.pop()) + rev
    return rev


print(reverseNumber(365))
