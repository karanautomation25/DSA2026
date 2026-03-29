# https://www.youtube.com/watch?v=agB1LyObUNE

class Solution:
    def findMaxLength(self, nums):

        zero = 0
        one = 0
        res = 0

        # stores (one - zero) → first index where it occurred
        diff_index = {}

        for i in range(len(nums)):

            if nums[i] == 0:
                zero = zero + 1
            else:
                one = one + 1

            diff = one - zero

            # store first occurrence
            if diff not in diff_index:
                diff_index[diff] = i

            # case when equal number of 0s and 1s from start
            if one == zero:
                res = one + zero
            else:
                idx = diff_index[diff]
                res = max(res, i - idx)

        return res


# Driver Code
nums = [0, 1, 0, 1, 1, 1, 0]

sol = Solution()
result = sol.findMaxLength(nums)

print("Input:", nums)
print("Max Length of Balanced Subarray:", result)