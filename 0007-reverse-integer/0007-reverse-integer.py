class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        res = 0
        curr = abs(x)
        sign = -1 if x < 0 else 1

        while curr:
            digit = curr % 10
            res = res * 10 + digit
            curr //= 10
        
        res *= sign
        return res if INT_MIN <= res <= INT_MAX else 0