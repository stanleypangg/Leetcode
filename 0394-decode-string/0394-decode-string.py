class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for i in range(len(s)):
            if s[i] != ']':
                st.append(s[i])
            else:
                substring = ''
                while st[-1] != '[':
                    substring = st.pop() + substring
                st.pop()

                k = ''
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k) * substring)
        
        return ''.join(st)