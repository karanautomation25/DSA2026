class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []  # (startIndex, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))

        n = len(heights)
        for index, height in stack:
            maxArea = max(maxArea, height * (n - index))

        return maxArea


if __name__ == "__main__":
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(s.largestRectangleArea(heights))   # Expected: 10