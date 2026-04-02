from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue

            # Decrease count of all elements
            new_count = defaultdict(int)
            for key, val in count.items():
                if val > 1:
                    new_count[key] = val - 1
            count = new_count

        # Final verification of candidates
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res

sol = Solution()
print(sol.majorityElement([1,1,1,3,3,2,2,2]))  # Output: [1, 2]