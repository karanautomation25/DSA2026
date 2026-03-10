# https://takeuforward.org/arrays/find-out-how-many-times-the-array-has-been-rotated/

# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3]
# Result: 4
# Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.


l = [4,5,6,7,0,1,2,3]
m = sorted(l)
count = 0

for i in range(len(m)-1,-1,-1):
    new_l = m[i:] + m[:i]
    count+=1
    if new_l == l:
        print(count)
        break
    new_l.clear()