# Maximum Sum Subarray of size K

a = [1, 2, 3, 4, 5, 6]
n = len(a)
k = 3

res = 0
for i in range(k):
    res += a[i]

max_sum = res
for i in range(k, n):
    res = res + a[i] - a[i - k]
    max_sum = max(res, max_sum)

print(max_sum)