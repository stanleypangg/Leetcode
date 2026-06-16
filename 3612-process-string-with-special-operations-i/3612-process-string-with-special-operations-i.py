class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for c in s:
            if c == '*':
                if res: res.pop()
            elif c == '#':
                res.extend(res)
            elif c == '%':
                res = list(reversed(res))
            else:
                res.append(c)
        
        return ''.join(res)