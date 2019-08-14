# 0 *
# 1
# 2 ****
# 3
# 4 **
data = [[0,1],[2,4],[4,2], [6,7],[8,5], [11,3]]
start = data[0][0]
end = data[len(data)-1][0]
index = 0
try:
    while start < end + 1 and index < len(data):
        if index < end - 1 and start == data[index][0]:
            print(str(data[index][0]) + " " + data[index][1] * "*")
            index = index + 1
        else:
            while start < data[index][0]-1:
                start = start + 1
                print(start)
            start = start + 1
except Exception as e:
    print(e)
    print(index)
    print(end)
