def rotateArrByReversal(arr, d):
    n = len(arr)
    reverseArr(arr,0, d-1)
    reverseArr(arr,d, n-1)
    reverseArr(arr,0, n-1)
    return arr


def reverseArr(arr, start, end):
    while start< end:
        t = arr[start]
        arr[start] = arr[end]
        arr[end] = t
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = 3

print("Before Rotation", arr)
print("After Rotation", rotateArrByReversal(arr, d))
