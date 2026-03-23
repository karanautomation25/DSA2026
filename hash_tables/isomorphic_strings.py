class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(sol.isIsomorphic("egg", "add"))   # True
    print(sol.isIsomorphic("foo", "bar"))   # False
    print(sol.isIsomorphic("paper", "title"))  # True
