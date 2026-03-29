# https://www.youtube.com/watch?v=P6RZZMu_maU

class Solution:
    def longestConsecutive(self, nums):

        numSet = set(nums)
        longest = 0

        for n in nums:

            # check if it is the start of a sequence
            if (n - 1) not in numSet:

                length = 0

                while (n + length) in numSet:
                    length = length + 1

                longest = max(length, longest)

        return longest


# Driver Code
nums = [100, 4, 200, 1, 3, 2]

sol = Solution()
result = sol.longestConsecutive(nums)

print("Input:", nums)
print("Longest Consecutive Sequence Length:", result)