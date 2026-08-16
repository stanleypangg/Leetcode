class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.list = [None] * k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.list[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.list[self.head] = None
        self.head = (self.head + 1) % self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.head == self.tail % self.k and self.list[self.head] is None

    def isFull(self) -> bool:
        return self.head == self.tail % self.k and self.list[self.head] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()