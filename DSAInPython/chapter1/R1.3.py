# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


def minmax_method1(data):
    data.sort()
    return [data[0], data[len(data)-1]]


def minmax_method2(data):
    min = max = data[0]
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    return [min, max]


if __name__ == "__main__":
    d = [-99, -1, -9, 0, 3, 4, 6, 8, 4, 3, 24, 6, 557, 7878]
    print minmax_method1(d)
    print minmax_method2(d)
