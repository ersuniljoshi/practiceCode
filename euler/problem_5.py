'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
n = 2520

divlist = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def divideByAll(num):
    count = len(divlist)
    n = 0
    for val in divlist:
        if num % val == 0:
            n = n + 1
    if n == count:
        return True
    else:
        return False

for i in range(1,1000000000):
    if divideByAll(i):
        print i
        break
