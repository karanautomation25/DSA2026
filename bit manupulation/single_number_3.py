def singleNumber(nums):
    d = {}
    res = []
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for k, v in d.items():
        if v == 1:
            res.append(k)
    return res


nums = [1,2,1,3,2,5]
print(singleNumber(nums))