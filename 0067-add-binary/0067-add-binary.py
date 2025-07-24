class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        carry = 0
        res = []

        while -i <= len(a) or -i <= len(b) or carry:
            summ = carry

            if -i <= len(a):
                summ += int(a[i])

            if -i <= len(b):
                summ += int(b[i])

            res.append(str(summ % 2))
            carry = summ // 2
            i -= 1
        
        return ''.join(reversed(res))