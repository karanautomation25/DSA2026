arr = [1,3,4,2,6,1]

k = 3
i=j=0
l = []
l2 = []
size = len(arr)

while j<size+1:
    if j-i+1 !=k+1:
        j+=1

    elif j-i+1 ==k+1:
        l2 = arr[i:j]
        max_val = max(l2)
        l.append(max_val)
        i+=1
        j+=1

print(l)