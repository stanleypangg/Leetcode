class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        if n <= 3:
            return n

        prev1 = 3
        prev2 = 2
        
        for _ in range(3, n):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr