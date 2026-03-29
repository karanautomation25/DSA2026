class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Calculates the maximum amount of water a container can store.
        Uses two-pointer approach with O(n) time and O(1) space.
        """

        # --------------------
        # BRUTE FORCE (O(n^2))
        # --------------------
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res

        # --------------------
        # OPTIMAL SOLUTION (O(n))
        # --------------------
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # Calculate area between two lines
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            # Move the pointer pointing to the smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


# ----------------------------
# Example usage / test cases
# ----------------------------
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    heights1 = [1,8,6,2,5,4,8,3,7]
    print("Input:", heights1)
    print("Max Water Area:", solution.maxArea(heights1))
    print()

    # Example 2
    heights2 = [1,1]
    print("Input:", heights2)
    print("Max Water Area:", solution.maxArea(heights2))
    print()

    # Example 3
    heights3 = [4,3,2,1,4]
    print("Input:", heights3)
    print("Max Water Area:", solution.maxArea(heights3))
    print()

    # Example 4
    heights4 = [1,2,1]
    print("Input:", heights4)
    print("Max Water Area:", solution.maxArea(heights4))
    print()