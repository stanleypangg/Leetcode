class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [s[0]]
        count = 1

        for i in range(1, len(s)):
            curr = s[i]

            if curr == res[-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                res.append(curr)
        
        return ''.join(res)