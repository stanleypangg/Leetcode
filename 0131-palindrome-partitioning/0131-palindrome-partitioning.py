class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def bt(curr, i):
            if i >= len(s) and is_palindrome(curr[-1]):
                self.res.append(curr.copy())
                return
            elif i >= len(s):
                return
            
            if curr:
                temp = curr[-1]
                curr[-1] += s[i]
                bt(curr, i + 1)
                curr[-1] = temp
            
            if not curr or is_palindrome(curr[-1]):
                curr.append(s[i])
                bt(curr, i + 1)
                curr.pop()
        
        bt([], 0)
        return self.res