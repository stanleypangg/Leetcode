class MedianFinder:

    def __init__(self):
        # All in self.max <= self.min
        self.max = []
        self.min = []
        self.insert = True # MAX = True, MIN = False

    def addNum(self, num: int) -> None:
        if self.insert:
            heapq.heappush(self.max, -num)
        else:
            heapq.heappush(self.min, num)
        
        while self.min and -self.max[0] > self.min[0]:
            max_tmp = -heapq.heappop(self.max)
            min_tmp = heapq.heappop(self.min)
            heapq.heappush(self.min, max_tmp)
            heapq.heappush(self.max, -min_tmp)
        
        self.insert = not self.insert

    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (-self.max[0] + self.min[0]) / 2
        else:
            return -self.max[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()