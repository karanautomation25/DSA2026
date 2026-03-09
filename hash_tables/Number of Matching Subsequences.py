from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s, words):

        table = defaultdict(deque)

        for ch in s:
            if ch not in table:
                table[ch] = deque()

        ans = 0

        for word in words:
            start_char = word[0]
            if start_char in table:
                table[start_char].append(word)

        for ch in s:
            q = table[ch]
            size = len(q)

            for _ in range(size):
                word = q.popleft()
                remaining = word[1:]

                if len(remaining) == 0:
                    ans += 1
                else:
                    next_char = remaining[0]
                    if next_char in table:
                        table[next_char].append(remaining)

        return ans


# driver code
s = "abcde"
words = ["a", "bb", "acd", "ace"]

sol = Solution()
print(sol.numMatchingSubseq(s, words))