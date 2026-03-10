

arr = [2,5,3,7,4,5,9,6,1]

size = len(arr)
i=j=0
k = 3
sum = 0
max_val = 0

while(j<size):
    sum = sum + arr[j]
    if j-i+1 != k:
        j+=1

    elif j-i+1 == k:
        max_val = max(max_val,sum)
        sum = sum - arr[i]
        i+=1
        j+=1


print(max_val)
