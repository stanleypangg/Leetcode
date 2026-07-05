class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.n = len(encoding)
        self.cur = 0

    def next(self, n: int) -> int:
        while self.cur < self.n and n > self.encoding[self.cur]:
            n -= self.encoding[self.cur]
            self.cur += 2

        if self.cur >= self.n:
            return -1
        
        self.encoding[self.cur] -= n
        return self.encoding[self.cur + 1]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)