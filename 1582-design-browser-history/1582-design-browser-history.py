class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.forward_hist = []
        self.backward_hist = []

    def visit(self, url: str) -> None:
        self.backward_hist.append(url) # visit url
        self.forward_hist = [] # clear forward history

    def back(self, steps: int) -> str:
        x = min(len(self.backward_hist), steps)
        for _ in range(x):
            nextt = self.backward_hist.pop()
            self.forward_hist.append(nextt)
        
        return self.homepage if not self.backward_hist else self.backward_hist[-1]

    def forward(self, steps: int) -> str:
        x = min(len(self.forward_hist), steps)
        for _ in range(x):
            nextt = self.forward_hist.pop()
            self.backward_hist.append(nextt)
        
        return self.homepage if not self.backward_hist else self.backward_hist[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)