class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.x = defaultdict(set)
        self.y = defaultdict(set)

    def add(self, point: List[int]) -> None:
        px, py = point
        self.freq[(px, py)] += 1
        self.x[px].add(py)
        self.y[py].add(px)

    def count(self, point: List[int]) -> int:
        res = 0
        ax, ay = point

        by = ay
        for bx in self.y[by]:
            dist = abs(ax - bx)
            if dist == 0:
                continue

            if ax in self.y[ay + dist] and bx in self.y[by + dist]:
                # square found
                cx, cy = ax, ay + dist
                dx, dy = bx, by + dist
                res += self.freq[(bx, by)] * self.freq[(cx, cy)] * self.freq[(dx, dy)]

            if ax in self.y[ay - dist] and bx in self.y[by - dist]:
                # square found
                cx, cy = ax, ay - dist
                dx, dy = bx, by - dist
                res += self.freq[(bx, by)] * self.freq[(cx, cy)] * self.freq[(dx, dy)]

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)