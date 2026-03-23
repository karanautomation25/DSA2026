# Neetcode solution

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest


if __name__ == "__main__":
    sol = Solution()
    
    # Example test cases
    nums = [100, 4, 200, 1, 3, 2]
    print("Longest Consecutive Sequence Length:", sol.longestConsecutive(nums))
