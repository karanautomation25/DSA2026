def minimumSubstringWindow(s, t):
    d = {}
    for i in t:
        if i in d:
            d[i]+=1
        else:
            d[i]=1






s = "ADOBECODEBANC"
t = "ABC"

result = minimumSubstringWindow(s, t)

print("Minimum Window Length:", result)