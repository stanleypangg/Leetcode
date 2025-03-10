class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            elif c == ')' and (not stack or stack.pop() != '('):
                return False
            elif c == ']' and (not stack or stack.pop() != '['):
                return False
            elif c == '}' and (not stack or stack.pop() != '{'):
                return False
        
        return not stack