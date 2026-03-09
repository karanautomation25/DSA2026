class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        prefix = [0] * n
        suffix = [0] * n

        pre_set = set()
        suf_set = set()

        for i in range(n):
            pre_set.add(s[i])
            suf_set.add(s[n - 1 - i])

            prefix[i] = len(pre_set)
            suffix[n - 1 - i] = len(suf_set)

        good_ways = 0

        for i in range(1, n):
            if prefix[i - 1] == suffix[i]:
                good_ways += 1

        return good_ways


# Driver code
s = "aacaba"

sol = Solution()
result = sol.numSplits(s)

print("Input:", s)
print("Good Splits:", result)




# mycode :
# def count_occurence(s):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
#
# def numSplits(s):
#     count=0
#     for i in range(len(s)):
#         a = s[:i]
#         b = s[i:]
#         dA = count_occurence(a)
#         dB = count_occurence(b)
#         if len(dA) == len(dB):
#             count+=1
#     return count
#
# s = 'aacaba'
# print(numSplits(s))