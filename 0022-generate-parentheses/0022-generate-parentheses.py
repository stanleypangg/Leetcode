class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(p, l, r):
            if l == 0 and r == 0:
                res.append(p)
            if l > 0:
                bt(p + '(', l - 1, r)
            if r > l:
                bt(p + ')', l, r - 1)
        
        bt('', n, n)

        return res