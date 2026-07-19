class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        n = len(word)

        def bt(i, abbr):
            if i >= n:
                res.append(abbr)
                return
            
            if not abbr or not abbr[-1].isdigit():
                for j in range(1, n - i + 1):
                    bt(i + j, abbr + str(j))
            
            bt(i + 1, abbr + word[i])
        
        bt(0, '')
        return res