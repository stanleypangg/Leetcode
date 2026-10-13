class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        for i, n in enumerate(num):
            while k > 0 and st and st[-1] > n:
                st.pop()
                k -= 1
            
            st.append(n)
        
        if k > 0:
            st = st[:-k]

        return ''.join(st).lstrip('0') or '0'