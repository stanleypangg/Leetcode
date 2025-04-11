class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: int(x / y),
            '*': lambda x, y: x * y
        }
        st = []

        for t in tokens:
            if t in operators:
                y, x = st.pop(), st.pop()
                st.append(operators[t](x, y))
            else:
                st.append(int(t))
        
        return st[0]