

def isPalindrome(str1):
    temp = str1[::-1]
    if temp == str1:
        return True
    else:
        return False

arr = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        num = i * j
        if isPalindrome(str(num)):
            arr.append(num)

arr.sort()
print arr[len(arr)-1]
