

arr = [12,-1,-7,8,-15,30,16,28]

size = len(arr)
i=j=0
k = 3
l = []
l2 = []

while(j<size):

    if arr[j]<0:
        l.append(arr[j])

    if j-i+1 != k:
        j+=1

    elif j-i+1 == k:

        if len(l) == 0:
            l2.append(0)
        else:
            l2.append(l[0])
            if arr[i] == l[0]:
                v = l.pop(0)

        i+=1
        j+=1

print(l2)