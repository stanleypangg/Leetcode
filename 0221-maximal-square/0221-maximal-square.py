class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[int(matrix[r][c]) for c in range(n)] for r in range(m)]
        best = max(dp[0] + [dp[r][0] for r in range(m)])

        for r in range(1, m):
            for c in range(1, n):
                if dp[r][c] == 0:
                    continue
                  
                dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                best = max(best, dp[r][c])
        
        return best ** 2