class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        above = matrix[0].copy()

        for row in range(1, n):
            cache = []
            
            for col in range(n):
                minimum = above[col]
                if col + 1 < n:
                    minimum = min(minimum, above[col + 1])
                if col - 1 >= 0:
                    minimum = min(minimum, above[col - 1])
                cache.append(minimum + matrix[row][col])

            above = cache
        
        return min(above)