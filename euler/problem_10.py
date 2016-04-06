import math

num = 2000000
sum = 17 # Sum of prime number below 10

def isPrime(num):
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0 :
            return False
    return True

for i in range(11,num-1):
    if isPrime(i):
        sum = sum + i
print sum
