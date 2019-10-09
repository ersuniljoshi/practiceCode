ls = [54, 546, 548, 60]

def myCompare(x , y):
    xy = str(x)  + str(y)
    yx = str(y) + str(x)
    if int(xy) >= int(yx):
        return 1
    else:
        return -1

def mySort(ls):
    for i in range(0, len(ls)):
        for j in (range(i, len(ls))):
            if myCompare(ls[i], ls[j]) == 1:
                pass
            else:
                ls[i], ls[j] = ls[j], ls[i]
        print ("After" + str(i) +" Iteration")
        print (ls)

mySort(ls)
