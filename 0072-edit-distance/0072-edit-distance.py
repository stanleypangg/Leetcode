class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1

        dp = [[0] * n for _ in range(m)]
        
        dp[0] = list(range(n))
        for r in range(m):
            dp[r][0] = r
        
        for r in range(1, m):
            for c in range(1, n):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    insert = dp[r - 1][c]
                    delete = dp[r][c - 1]
                    replace = dp[r - 1][c - 1]
                    dp[r][c] = 1 + min(insert, delete, replace)
        
        return dp[m - 1][n - 1]