arr = [2, 3, 9, 5, 78, 3, 2, 5, 7, 12, 0, 67, 34]


def binarySearch(arr, l, r, key):
    if l < r:
        m = (r + l)/2
        if arr[m] == key:
            return "Found"
        if arr[m] < key:
            return binarySearch(arr, m+1, r, key)
        if arr[m] > key:
            return binarySearch(arr, l, m-1, key)

    return "Element doesnot exists!!"


if __name__ == '__main__':
    #  arr.sort()
    print binarySearch(arr, 0, len(arr), 9)
