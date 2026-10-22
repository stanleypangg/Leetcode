class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        matrix = [[int(num) for num in matrix[r]] for r in range(m)]

        above = matrix[0]
        best = max(above)

        for r in range(1, m):
            left = matrix[r][0]
            best = max(best, left)
            row = [0] * n
            row[0] = left

            for c in range(1, n):
                if matrix[r][c] == 1:
                    row[c] = 1 + min(left, above[c - 1], above[c])
                left = row[c]
                best = max(best, row[c])
            
            above = row
            
        return best ** 2