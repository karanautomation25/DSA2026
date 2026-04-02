def majorityElement(nums):
    res = 0
    count = 0

    for n in nums:

        # Step 1: If count becomes 0,
        # choose current element as new candidate
        if count == 0:
            res = n

        # Step 2: If current element matches candidate
        if n == res:
            count = count + 1
        else:
            count = count - 1

    return res

nums = [1,2,1,1,2,2,2,1,2,2,2]
print(majorityElement(nums))