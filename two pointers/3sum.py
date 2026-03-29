from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, a in enumerate(nums):
            # Skip duplicate values for the first element
            if i > 0 and a == nums[i - 1]:
                continue

            # Two-pointer approach
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.add((a, nums[l], nums[r]))
                    l += 1

                    # Skip duplicate values for the left pointer
                    # while l < r and nums[l] == nums[l - 1]:
                    #     l += 1

        return list(res)


# --------------------------
# CALLABLE EXAMPLES HERE
# --------------------------
if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("Input:", nums1)
    print("3Sum:", s.threeSum(nums1))

    # Example 2
    nums2 = [0, 1, 1]
    print("\nInput:", nums2)
    print("3Sum:", s.threeSum(nums2))

    # Example 3
    nums3 = [0, 0, 0]
    print("\nInput:", nums3)
    print("3Sum:", s.threeSum(nums3))