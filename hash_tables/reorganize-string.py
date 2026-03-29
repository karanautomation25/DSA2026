# https://www.youtube.com/watch?v=2g_b1aYTHeg

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:

        # count frequency of characters
        count = Counter(s)

        # build max heap (negative count because Python has min heap)
        maxHeap = []
        for char, cnt in count.items():
            maxHeap.append([-cnt, char])

        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap or prev:

            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)

            res = res + char
            cnt = cnt + 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res


# Driver code
s = "aaabb"

sol = Solution()
result = sol.reorganizeString(s)

print("Input:", s)
print("Reorganized String:", result)