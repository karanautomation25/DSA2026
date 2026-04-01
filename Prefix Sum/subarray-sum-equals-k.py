# Neetcode - https://www.youtube.com/watch?v=fFVZt-6sgyo

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}  # base case

        for n in nums:
            curSum += n
            diff = curSum - k

            # check if diff exists
            if diff in prefixSums:
                res += prefixSums[diff]

            # update hashmap
            if curSum in prefixSums:
                prefixSums[curSum] += 1
            else:
                prefixSums[curSum] = 1

        return res


# --------- Callable Example ---------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 1]
    k = 2

    result = sol.subarraySum(nums, k)
    print("Number of subarrays:", result)