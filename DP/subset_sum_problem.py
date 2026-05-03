def findSubsetSum_Elements(arr, target):
    n = len(arr)

    # ---------------------------------------------------------
    # PART 1: Build the DP Table (Exact same as before)
    # ---------------------------------------------------------
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    # If no subset exists, stop here and return None
    if not dp[n][target]:
        return None

    # ---------------------------------------------------------
    # PART 2: Backtrack to find the elements
    # ---------------------------------------------------------
    subset = []
    i = n  # Start at the last row (all items considered)
    j = target  # Start at the target sum column

    while i > 0 and j > 0:
        # Check if the value came from the row directly above
        # If it did, it means we DID NOT need the current element
        if dp[i - 1][j] == True:
            i -= 1  # Just move up

        # If it didn't come from above, we MUST HAVE included the current element
        else:
            subset.append(arr[i - 1])  # Add element to our result
            j -= arr[i - 1]  # Reduce the target sum by the element's value
            i -= 1  # Move up to the previous row

    # The subset is found backward, so reverse it (optional, but looks cleaner)
    subset.reverse()
    return subset


# ==========================================
# Driver Code to test the function
# ==========================================

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

    # Example 2: Testing a different target
    target2 = 30
    result2 = findSubsetSum_Elements(arr, target2)
    print(f"\nTarget: {target2} -> {result2}")