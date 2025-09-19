import random

class Solution:

    def __init__(self, w: List[int]):
        # w is a list of weights
        self.ranges = [0]
        for weight in w:
            self.ranges.append(self.ranges[-1] + weight)

    def pickIndex(self) -> int:
        random_num = self.ranges[-1] * random.random()
        l, r = 1, len(self.ranges) - 1
        while l < r:
            mid = (l + r) // 2
            if self.ranges[mid] < random_num:
                l = mid + 1
            else:
                r = mid
        return l - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()