class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []

        for i, c in enumerate(s):
            if c == '(':
                st.append(c)
            else:
                if st[-1] == '(':
                    st[-1] = 1
                elif st and len(st) >= 2 and st[-2] == '(' and isinstance(st[-1], int):
                    top = st.pop()
                    st[-1] = top * 2         

                while st and len(st) >= 2 and isinstance(st[-2], int):
                    top = st.pop()
                    st[-1] += top
            
            print(i, c, st)
 
        return st[0]