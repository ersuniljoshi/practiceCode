def rotateArrByJugglingAlgo(arr, d):
    lenarr = len(arr)
    mygcd = gcd(lenarr, d)
    for i in range(mygcd):
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= lenarr:
                k = k - lenarr
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    return arr



def gcd(a, b):
    while b:
        a,b =b, a%b
    return a


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = 6

print("Before Rotation", arr)
print("After Rotation", rotateArrByJugglingAlgo(arr, d))
