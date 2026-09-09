class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        res = 0
        x = 1000

        while x <= n:
            res += n - x + 1
            x *= 1000
        
        return res