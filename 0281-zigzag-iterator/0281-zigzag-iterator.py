class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = deque()
        if v1:
            self.q.append((v1, 0))
        if v2:
            self.q.append((v2, 0))

    def next(self) -> int:
        vec, idx = self.q.popleft()
        val = vec[idx]

        if idx + 1 < len(vec):
            self.q.append((vec, idx + 1))
        
        return val

    def hasNext(self) -> bool:
        return bool(self.q)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())