def findSubsetSum_Elements(arr, target):
    n = len(arr)
    dp = []
    for i in range(len(arr)):
        row = []
        for j in range(target+1):
            row.append(False)
        dp.append(row)

    for i in range(len(arr)):
        dp[i][0] = True

    for i in range(1,target):
        dp[0][i] = False

    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            if arr[i-1] < j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i - 1][j]

    if not dp[len(arr)][target]:
        return None
    res = []
    j = target
    i = len(arr)
    while j <= 0 and i <=0:
        if dp[i-1][j] == True:
            i-=1
        else:
            res.append(arr[i - 1])
            i -= 1
            j = j - arr[i - 1]



if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    target = 9

    print(f"Array: {arr}")
    print(f"Target: {target}")

    result = findSubsetSum_Elements(arr, target)

    if result:
        print(f"Subset found! The elements are: {result}")
    else:
        print("No valid subset exists.")
