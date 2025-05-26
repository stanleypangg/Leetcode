class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for c in s:
            res.append(c.lower())
        return ''.join(res)