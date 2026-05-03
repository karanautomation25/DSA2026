from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Step 1: handle k > n
        n = len(nums)
        k = k % n

        # Helper function to reverse elements
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 2: reverse entire array
        reverse(0, n - 1)

        # Step 3: reverse first k elements
        reverse(0, k - 1)

        # Step 4: reverse remaining elements
        reverse(k, n - 1)


# 🔥 Callable Example
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    obj = Solution()
    obj.rotate(nums, k)

    print("Rotated Array:", nums)