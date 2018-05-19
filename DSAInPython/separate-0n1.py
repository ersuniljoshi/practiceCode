def separate0n1(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] ==0:
            l +=1
        elif arr[r] == 1:
            r -= 1
        elif arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -=1
    return arr

print (separate0n1([0 ,1 , 1, 1,1, 0, 1, 1,0,0]))
