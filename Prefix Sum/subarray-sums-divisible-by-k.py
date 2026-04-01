#Neetcode - https://www.youtube.com/watch?v=bcXy-T4Sc3E

from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0

        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            res += prefix_cnt[remain]
            prefix_cnt[remain] += 1

        return res


# --------- Example Run ---------
if __name__ == "__main__":
    sol = Solution()

    nums = [4, 5, 0, -2, -3, 1]
    k = 5

    result = sol.subarraysDivByK(nums, k)
    print("Count of subarrays divisible by k:", result)