class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == '+':
                st.append(st.pop() + st.pop())
            elif t == '-':
                b, a = st.pop(), st.pop()
                st.append(a - b)
            elif t == '*':
                st.append(st.pop() * st.pop())
            elif t == '/':
                b, a = st.pop(), st.pop()
                st.append(int(a / b))
            else:
                st.append(int(t))
        
        return st[0]