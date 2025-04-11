class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == '(':
                st.append('(')
            elif c == '[':
                st.append('[')
            elif c == '{':
                st.append('{')
            elif c == ')' and (not st or st.pop() != '('):
                return False
            elif c == ']' and (not st or st.pop() != '['):
                return False
            elif c == '}' and (not st or st.pop() != '{'):
                return False
        
        return not st