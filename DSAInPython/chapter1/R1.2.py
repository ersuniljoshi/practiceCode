# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return False if k & 1 != 0 else True

if __name__ =="__main__":
    print is_even(4)
