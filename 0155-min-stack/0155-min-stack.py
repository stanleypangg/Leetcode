class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if val < self.getMin():
            self.st.append((val, val))
        else:
            self.st.append((val, self.getMin()))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        if not self.st:
            return float('inf')
        else:
            return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()