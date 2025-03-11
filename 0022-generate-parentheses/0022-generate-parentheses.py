class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = []

        def bt(l, r):
            if l == 0 and r == 0:
                res.append(''.join(st))
            if l > 0:
                st.append('(')
                bt(l - 1, r)
                st.pop()
            if r > l:
                st.append(')')
                bt(l, r - 1)
                st.pop()
        
        bt(n, n)

        return res