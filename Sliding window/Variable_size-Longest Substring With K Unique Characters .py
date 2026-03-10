str = 'aabacaabebebe'
size = len(str)
k = 3
d = {}
i=j=0
mx = 0
c = 1

while j<size:

    if str[j] in d:
        d[str[j]] = d[str[j]] + 1
    else:
        d[str[j]] = c
    if len(d) < k:
        j+=1
    elif len(d) == k:
        mx = max(mx,j-i+1)
        j+=1
    elif len(d) > k:
        while(len(d)>k):
            d[str[i]] = d[str[i]] - 1
            if d[str[i]] == 0:
                d.pop(str[i])
            i+=1
        j+=1

print(mx)
