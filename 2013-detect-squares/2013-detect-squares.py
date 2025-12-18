class DetectSquares:

    def __init__(self):
        # key by x -> y -> frequency
        self.coords = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.coords[x][y] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for y2 in self.coords[x1]:
            if y1 == y2:
                continue
            dist = abs(y1 - y2)
            res += self.coords[x1][y2] * self.coords[x1 + dist][y1] * self.coords[x1 + dist][y2]
            res += self.coords[x1][y2] * self.coords[x1 - dist][y1] * self.coords[x1 - dist][y2]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)