def separate0n1(arr):
    l = 0
    r = len(arr) - 1
    m = (l + r )//2
    while l < r:
        if arr[m] == 2 and arr[m]:
            arr[m], arr[r] = arr[r], arr[m]
            r -=1
            m +=1
        elif arr[m] == 1:
            r -= 1
        elif arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -=1
    return arr

print ( separate0n1([0 ,1 , 2, 2, 1, 0,2,0,1,1, 1,1, 0, 1, 1,0,0]) )
