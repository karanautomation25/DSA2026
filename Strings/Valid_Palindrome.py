class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1

            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l = l + 1
            r = r - 1

        return True

    def alphaNum(self, c):
        return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
        )


# Test
sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))  # False


# # my code :
#
# def sPalindrome(s):
#     s = s.strip()
#     res = []
#     num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for i in s:
#         i = i.lower()
#         if ord(i) >= 97 and ord(i) <= 122 or i in num:
#             res.append(i)
#     s = ''.join(res)
#     t = s[::-1]
#     if s == t:
#         return True
#     else:
#         return False
#
#
# # s = "0P"
# s = "A man, a plan, a canal: Panama"
# # s = "azAZ"
# print(sPalindrome(s))
#
