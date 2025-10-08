class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = 0
        self.bound = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr += 1
        if len(self.history) == self.curr:
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)