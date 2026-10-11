class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        st = []

        for c in s:
            if c == '(':
                if st and st[-1] == ')':
                    st.pop()
                    st.pop()
                    res += 1
                st.append(c)
            else:
                if st and st[-1] == ')':
                    st.pop()
                    st.pop()
                elif not st:
                    st.append('(')
                    st.append(c)
                    res += 1
                else:
                    st.append(c)

        if st: 
            if st[-1] == ')':
                res += 1
            else:
                res += 2

        return res