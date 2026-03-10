# https://www.youtube.com/watch?v=Ty8EZlxVNC8

from collections import defaultdict

class Solution:
    def isPossible(self, nums):

        availability = defaultdict(int)
        vacancy = defaultdict(int)

        # count frequency
        for num in nums:
            availability[num] += 1

        for num in nums:

            if availability[num] <= 0:
                continue

            # case 1: extend existing subsequence
            elif vacancy[num] > 0:

                availability[num] -= 1
                vacancy[num] -= 1
                vacancy[num + 1] += 1

            # case 2: create new subsequence num,num+1,num+2
            elif availability[num] > 0 and availability[num + 1] > 0 and availability[num + 2] > 0:

                availability[num] -= 1
                availability[num + 1] -= 1
                availability[num + 2] -= 1

                vacancy[num + 3] += 1

            else:
                return False

        return True

nums = [1,2,3,3,4,4,5,5]

sol = Solution()
print(sol.isPossible(nums))