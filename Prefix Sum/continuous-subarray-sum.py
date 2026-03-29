# https://www.youtube.com/watch?v=OKcrLfR-8mE
class Solution:
    def checkSubarraySum(self, nums, k):

        # remainder -> first index
        remainder_map = {0: -1}

        total = 0

        for i in range(len(nums)):
            total += nums[i]

            # handle k != 0 case
            if k != 0:
                total = total % k

            if total not in remainder_map:
                remainder_map[total] = i
            else:
                # subarray length should be at least 2
                if i - remainder_map[total] > 1:
                    return True

        return False


# Driver Code
nums = [23, 2, 4, 6, 7]
k = 6

sol = Solution()
print("Input:", nums, "k =", k)
print("Output:", sol.checkSubarraySum(nums, k))