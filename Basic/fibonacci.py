# 1, 2, 3, 5, 8, 13, 21, 34, 55

n = 9

a = 1
b = 1
x = 0

while x < (n-1) :
    sum = a+b
    a = b
    b = sum
    x+=1

print(sum)

