# Largest Subarray of sum K


A = [4, 1, 1, 1, 2, 3, 5]
k = 5

n = len(A)

i = 0
j = 0
total = 0
maxL = float('-inf')

while j < n:

    # 1. Calculation
    total += A[j]

    if total < k:
        j += 1

    elif total == k:
        maxL = max(maxL, j - i + 1)
        j += 1
    else:
        while total > k:
            total -= A[i]
            i += 1
        j += 1

print(f"Largest Subarray of Sum {k} has size: ", maxL)