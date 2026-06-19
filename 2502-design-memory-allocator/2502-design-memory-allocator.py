class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = [True] * n
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        if size > self.n:
            return -1

        window = {True: 0, False: 0}
        for i in range(size):
            window[self.memory[i]] += 1
        
        l, r = 0, size
        while r < self.n and window[False] > 0:
            window[self.memory[l]] -= 1
            window[self.memory[r]] += 1
            l += 1
            r += 1
        
        if window[False]:
            return -1

        self.memory[l:r] = [False] * size
        self.blocks[mID].append((l, r))
        return l

    def freeMemory(self, mID: int) -> int:
        res = 0
        while self.blocks[mID]:
            start, end = self.blocks[mID].pop()
            for i in range(start, end):
                self.memory[i] = True
                res += 1
        return res


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)