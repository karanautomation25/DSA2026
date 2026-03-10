class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n
        stack = []  # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prevTemp, prevIndex = stack.pop()
                res[prevIndex] = i - prevIndex
            stack.append([t, i])

        return res


# ---------------------------
# Example run
# ---------------------------
if __name__ == "__main__":
    s = Solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temps))