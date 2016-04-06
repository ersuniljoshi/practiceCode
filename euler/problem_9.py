tot = 1000

for i in range(1000,1,-1):
    num1 = i
    num2 = 1000 - i
    num3 = 1000 - num2
    if (num1^2 + num2^2 == num3^2):
        print num1, num2 , num3
        break

print num1*num2*num3
