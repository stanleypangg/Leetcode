class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        elif n == 2:
            return k * k
        
        one, two = k * k, k
        for _ in range(3, n + 1):
            one, two = (one + two) * (k - 1), one
        
        return one