# Maximum of all subarrays of size k

arr = [1,2,4]
k=3
i = j = 0
temp = []
result = []
n = len(arr)


while j < n:
    if temp == [] or (temp[0] >= arr[j] and temp[-1] >= arr[j]):
        temp.append(arr[j])
    else:
        while temp != [] and temp[-1] < arr[j]:
            temp.pop()
        temp.append(arr[j])
    if j - i + 1 == k:
        result.append(temp[0])
        if temp[0] == arr[i]:
            temp.pop(0)
        i += 1
    j += 1

print(result)

