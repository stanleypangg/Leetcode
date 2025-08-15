class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''

        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                if res == '' or res < num[i]:
                    res = num[i]
        
        return res * 3
