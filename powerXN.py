__author__ = 'sjoshi'

# Complexity is O(log n)
def powerXNRecursion(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return powerXNRecursion(x,n/2)*powerXNRecursion(x,n/2)
    else:
        return x*powerXNRecursion(x,n/2)*powerXNRecursion(x,n/2)

# Complexity is O(n)
def powerXNIterative(x,n):
    answer = 1
    if n==0:
        return 1
    else:
        for i in range(n):
            answer = answer*x
    return answer

print powerXNRecursion(1,1)
print powerXNIterative(3,3)
