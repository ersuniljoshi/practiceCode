M = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]

num = 99

rows = len(M)
columns = len(M[0])

tc = columns - 1
tr = 0
found = False
while (tr < rows- 1) and tc >= 0:
    print "Debug", tr, tc
    if M[tr][tc] == num:
        found = True
        print tr, tc
        break
    if num > M[tr][tc]:
        tr += 1
    if num < M[tr][tc]:
        tc -= 1

if not found:
    print ( "Element Doesnot Exists" )
