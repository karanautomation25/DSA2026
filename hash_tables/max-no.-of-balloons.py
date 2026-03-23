# Neetcode solution

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)
        for c in balloon:
            res = min(res, countText[c] // balloon[c])

        return res


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(sol.maxNumberOfBalloons("nlaebolko"))      # 1
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))  # 2
    print(sol.maxNumberOfBalloons("leetcode"))       # 0
