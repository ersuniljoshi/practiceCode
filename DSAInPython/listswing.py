def swing(arr):
    counter = True
    for i in range(0,len(arr)-2):
        if counter and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        if not counter and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        counter = bool(1- counter)
    return arr


l = [4, 3 ,7 , 8 ,6 ,2, 1]
print swing(l)
