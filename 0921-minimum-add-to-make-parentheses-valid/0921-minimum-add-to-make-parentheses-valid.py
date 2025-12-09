class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = balance = 0

        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance == 0:
                    res += 1
                else:
                    balance -= 1
        
        return res + abs(balance)