class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        i = 0
        while i < len(path):
            curr = path[i]

            # Clear any slashes
            while i < len(path) and path[i] == '/':
                i += 1
            
            if i == len(path):
                break

            if i < len(path) and path[i] == '.' and (i == len(path) - 1 or path[i + 1] == '/'):
                # Current diectory
                i += 2
            elif i < len(path) - 1 and path[i] == path[i + 1] == '.' and (i == len(path) - 2 or path[i + 2] == '/'):
                # Previous directory
                if stack:
                    stack.pop()
                i += 3
            else:
                l = r = i
                while r < len(path) and path[r] != '/':
                    r += 1
                stack.append(path[l: r])            
                i = r
        
        return '/' + '/'.join(stack)