# https://youtu.be/ypn0aZ0nrL4?si=xHzzIKtHWvk4dd05

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True

            window.add(nums[R])

        return False


# ---- Example usage ----
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3

    sol = Solution()
    result = sol.containsNearbyDuplicate(nums, k)
    print(result)  # Expected: True
