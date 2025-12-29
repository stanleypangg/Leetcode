class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        res = []
        for n in mapping:
            multiples = num // n
            if multiples > 0:
                res.append(multiples * mapping[n])
                num -= multiples * n

        return ''.join(res)