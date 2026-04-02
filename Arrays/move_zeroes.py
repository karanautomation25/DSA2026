# https://www.youtube.com/watch?v=aayNRwUN3Do

def moveZeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r]!=0:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1

    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

# [1, 0, 0, 3, 12]