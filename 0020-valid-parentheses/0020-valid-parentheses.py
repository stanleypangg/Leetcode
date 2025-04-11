class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {'(':')', '[':']', '{':'}'}

        for c in s:
            if c in mapping.keys():
                st.append(mapping[c])
            elif c in mapping.values() and not st or st.pop() != c:
                return False

        return not st