class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        self.valid = 0
        self.cur = 0

    def add(self, num: int) -> None:
        self.cur += 1
        if num == 0:
            self.valid = self.cur
            self.product = [1]
        elif not self.product:
            self.product.append(num)
        else:
            last = self.product[-1]
            self.product.append(last * num)

    def getProduct(self, k: int) -> int:
        if self.cur - k >= self.valid:
            return self.product[-1] // self.product[-k - 1]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)