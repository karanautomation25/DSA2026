# Remove Duplicate Letters - LeetCode 316
# Exact logic from your shared snippet (Techdose monotonic stack solution)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Step 1: Count frequency of each character
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        # Step 2: Track if a character is already in the stack
        seen = {c: False for c in s}

        # Step 3: Use a monotonic stack
        stack = []

        for ch in s:
            freq[ch] -= 1  # This char is now used once

            # If already added, skip
            if seen[ch]:
                continue

            # Maintain lexicographically smallest sequence
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                removed = stack.pop()
                seen[removed] = False   # Mark removed char as not present

            # Add new element
            stack.append(ch)
            seen[ch] = True

        # Final answer
        return "".join(stack)


# ----------------------------
# Callable Test Function
# ----------------------------

def run_examples():
    sol = Solution()

    examples = [
        "bcabc",      # expected "abc"
        "cbacdcbc",   # expected "acdb"
        "bbcaac",     # expected "bac"
        "cdadabcc",   # expected "adbc"
    ]

    for s in examples:
        print(f"Input: {s}")
        print(f"Output: {sol.removeDuplicateLetters(s)}")
        print("-" * 30)


# Run examples
if __name__ == "__main__":
    run_examples()