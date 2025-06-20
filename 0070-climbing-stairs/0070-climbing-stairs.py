class Solution:
    def climbStairs(self, n: int) -> int:
        # f(1) = 1, f(2) = 2
        # f(n) = f(n - 1) + f(n - 2) for n > 2

        if n <= 2:
            return n

        dp = [1, 2]
        for _ in range(n - 2):
            tmp = dp[1]
            dp[1] = tmp + dp[0]
            dp[0] = tmp
        
        return dp[1]