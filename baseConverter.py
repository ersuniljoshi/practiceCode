__author__ = 'sjoshi'

import myStack


def decimal_to_BaseConverterIteration(n, base):

    digits = "0123456789ABCDEF"
    s = myStack.Stack()
    strBin = ""
    while n>0:
        rem = n%base
        s.push(rem)
        n = n // base

    while not s.isEmpty():
        strBin = strBin + str(digits[s.pop()])

    return strBin

def decimal_to_BaseConverterRecursion(n, base):
    digits = "0123456789ABCDEF"
    if n <base:
        return digits[n]
    else:
        return decimal_to_BaseConverterRecursion(n//base,base) + str(digits[n%base])


print decimal_to_BaseConverterRecursion(1000,2)
print decimal_to_BaseConverterIteration(1000,2)