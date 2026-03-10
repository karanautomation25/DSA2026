class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            current_min = self.minStack[-1]
            if val < current_min:
                self.minStack.append(val)
            else:
                self.minStack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# ---------------------------
# Example Usage (callable)
# ---------------------------
if __name__ == "__main__":
    minStack = MinStack()

    minStack.push(5)
    minStack.push(3)
    minStack.push(7)
    minStack.push(2)

    print("Top:", minStack.top())            # 2
    print("Min:", minStack.getMin())         # 2

    minStack.pop()
    print("Min after pop:", minStack.getMin())   # 3