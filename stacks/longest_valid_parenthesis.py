# https://www.youtube.com/watch?v=gqQsbdTcey0&t=1011s

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack will store indices
        stack = []
        # Push -1 as a base index
        stack.append(-1)

        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                # Push index of '('
                stack.append(i)
            else:
                # Pop previous index
                stack.pop()

                if not stack:
                    # No base to measure from, push current index
                    stack.append(i)
                else:
                    # Calculate valid length
                    max_len = max(max_len, i - stack[-1])

        return max_len


# --------------------------------------
# Callable test casesaaa
# --------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    s1 = "(()"
    print(f"Input: {s1}")
    print("Output:", sol.longestValidParentheses(s1))
    # Expected: 2

    # Example 2
    s2 = ")()())"
    print(f"\nInput: {s2}")
    print("Output:", sol.longestValidParentheses(s2))
    # Expected: 4

    # Example 3
    s3 = "()(())"
    print(f"\nInput: {s3}")
    print("Output:", sol.longestValidParentheses(s3))
    # Expected: 6