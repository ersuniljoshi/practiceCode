# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.


def sumofSquares(n):
    total = 0
    total = sum(x*x for x in range(1, n))
    return total


if __name__ == "__main__":
    print sumofSquares(3)
