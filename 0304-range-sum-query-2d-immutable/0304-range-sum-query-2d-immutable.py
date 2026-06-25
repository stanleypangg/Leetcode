class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            row_prefix = 0

            for c in range(n):
                cur = matrix[r][c]
                self.prefix[r + 1][c + 1] += self.prefix[r][c + 1] + row_prefix + cur
                row_prefix += cur
        
        self.m = m
        self.n = n
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_strip = self.prefix[row2 + 1][col1]
        top_strip = self.prefix[row1][col2 + 1]
        overlap = self.prefix[row1][col1]
        base = self.prefix[row2 + 1][col2 + 1]

        return base + overlap - top_strip - left_strip

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)