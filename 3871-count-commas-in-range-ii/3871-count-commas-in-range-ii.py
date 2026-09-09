class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        mult = 1
        base = 10 ** (mult * 3)

        while n - base >= 0:
            res += (min(n, base * 1000 - 1) - 10 ** (mult * 3) + 1) * mult
            mult += 1
            base = 10 ** (mult * 3)
        
        return res