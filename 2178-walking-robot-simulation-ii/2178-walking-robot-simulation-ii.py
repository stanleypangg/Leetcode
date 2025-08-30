class Robot:

    def __init__(self, width: int, height: int):
        # track location
        self.x = self.y = 0
        self.width = width
        self.height = height
        self.facing = 0
        self.directions = ['East', 'North', 'West', 'South'] # E, N, W, S
        self.mod = 2 * (self.width + self.height - 2)

    def step(self, num: int) -> None:
        # 1. move forwrd one cell in direction its facing
        # 2. if OOB, turns 90 degrees counter clockwise and retries

        if num >= self.mod:
            num %= self.mod
            if self.x == self.y == self.facing == 0:
                self.facing = 3

        # don't have to keep looping
        while num > 0:
            if self.facing == 0:
                steps = min(num, self.width - self.x - 1)
                self.x += steps
            elif self.facing == 1:
                steps = min(num, self.height - self.y - 1)
                self.y += steps
            elif self.facing == 2:
                steps = min(num, self.x)
                self.x -= steps
            else:
                steps = min(num, self.y)
                self.y -= steps
            
            num -= steps
            
            if num > 0:
                self.facing = (self.facing + 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.facing]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()