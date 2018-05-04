def spiralMatrix(m , R, C):
    rs, re, cs, ce = 0, R-1, 0, C-1
    for i in range(0,ce):
        print m[rs][i],
    rs += 1


    for j in range(0,re):
        print m[j][ce],
    ce -= 1


m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

if __name__ == "__main__":
    spiralMatrix(m, R=4, C=5)
