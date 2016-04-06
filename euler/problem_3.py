'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
num = 600851475143

def isPrime(num):
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

for i in range(int(math.sqrt(600851475143)),2,-1):
    if num % i == 0:
        if isPrime(i):
            print i
            break
