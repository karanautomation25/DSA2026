class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1

        while i >= 0:
            # Skip trailing spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            # Find the start of the word
            j = i
            while j >= 0 and s[j] != " ":
                j -= 1

            # Add the word to result
            res.append(s[j+1:i+1])

            # Move pointer for next iteration
            i = j - 1

        return " ".join(res)


# ========== Example Usage ==========
if __name__ == "__main__":
    s = "  the sky   is blue  "
    sol = Solution()
    output = sol.reverseWords(s)

    print("Input:  ", repr(s))
    print("Output: ", repr(output))