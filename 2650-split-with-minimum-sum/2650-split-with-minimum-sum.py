class Solution:
    def splitNum(self, num: int) -> int:
        num_arr = sorted([n for n in str(num)])
        num1 = num2 = ''

        for n in num_arr:
            if len(num1) == len(num2):
                num1 += n
            else:
                num2 += n
            
        return int(num1) + int(num2)