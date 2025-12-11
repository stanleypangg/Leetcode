class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        curr = abs(x)
        is_neg = x < 0

        while curr >= 10:
            digit = curr % 10
            res = res * 10 + digit
            curr //= 10
        
        res = res * 10 + curr
        if is_neg:
            res *= -1

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res