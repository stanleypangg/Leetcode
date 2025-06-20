class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0, 1]
        
        for _ in range(n - 1):
            tmp = dp[1]
            dp[1] = dp[0] + tmp
            dp[0] = tmp
        
        return dp[1]