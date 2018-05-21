a = [1, 3, 2, 4, 7, 6, 9, 10]
l = 0
r = len(a) -1
print("Before", a)
while l < r:
    if a[l] % 2 == 0:
        l += 1
    else:
        if a[r] % 2 == 0:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        else:
            r -= 1

print("After", a)
