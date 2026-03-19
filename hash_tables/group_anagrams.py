#https://youtu.be/vzdNOK2oB2E?si=DgTyo9NrlrBNu8dT

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26  # for 'a' to 'z'

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())


# ---- Example usage ----
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    result = sol.groupAnagrams(strs)
    print(result)
