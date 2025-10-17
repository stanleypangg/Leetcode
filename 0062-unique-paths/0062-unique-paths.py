class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = # of unique paths to i, j
        # for all j dp[0][j] = 1
        # for all i dp[i][0] = 1
        # else dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        above = [1] * n
        dp = [1] * n

        # iterate all grids not on first row and first column
        for r in range(1, m):
            for c in range(1, n):
                dp[c] = above[c] + dp[c - 1]
            above = dp
            dp = [1] * n
        
        return above[-1]