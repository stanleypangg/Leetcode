class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.big = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            heapq.heappush(self.small, -heapq.heappushpop(self.big, num))
        else:
            heapq.heappush(self.big, -heapq.heappushpop(self.small, -num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (-self.small[0] + self.big[0]) / 2
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()