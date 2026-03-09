def singleNumber(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for k,v in d.items():
        if v==1:
            return k

nums = [2,2,1]
print(singleNumber(nums))