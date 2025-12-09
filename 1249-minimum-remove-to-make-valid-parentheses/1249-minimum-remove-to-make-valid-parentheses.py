class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = [] # carries indices of opening parenthese
        to_remove = set()

        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                if st:
                    st.pop()
                else:
                    to_remove.add(i)
        
        # remainder opening brackets that are never closed
        for i in st:
            to_remove.add(i)
        
        return ''.join(s[i] for i in range(len(s)) if i not in to_remove)