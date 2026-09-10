class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.k = k
        self.val = value

    def consec(self, num: int) -> bool:
        if num != self.val:
            self.count = 0
            return False
        
        # num == value
        self.count += 1
        if self.count < self.k:
            return False
        
        # if self.count >= self.k
        return True

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)