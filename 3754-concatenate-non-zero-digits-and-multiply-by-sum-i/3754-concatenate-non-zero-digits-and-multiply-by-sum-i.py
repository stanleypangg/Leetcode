class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        digits = []

        for num in str(n):
            if num != '0':
                digits.append(num)
                total += int(num)

        if total == 0:
            return 0
            
        res = ''.join(digits)
        return int(res) * total