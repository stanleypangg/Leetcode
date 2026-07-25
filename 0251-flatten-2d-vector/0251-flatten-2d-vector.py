class Vector2D:

    def _next_valid_row(self):
        while self.row < len(self.vec) and not self.vec[self.row]:
            self.row += 1

    def __init__(self, vec: List[List[int]]):
        # keep an inner and outer pointer
        self.vec = vec
        self.row = 0
        self.col = 0

        self._next_valid_row()

    def next(self) -> int:
        # invariant, at the beginning of next and hasNext, make sure we have 
        # self.row and self.col pointing to a valid elem
        val = self.vec[self.row][self.col]

        if self.col + 1 >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0
        else:
            self.col += 1

        self._next_valid_row()
        return val

    def hasNext(self) -> bool:
        return self.row < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()