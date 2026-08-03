class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {c for c in 'qwertyuiop'}
        second = {c for c in 'asdfghjkl'}
        third = {c for c in 'zxcvbnm'}

        res = []
        for w in words:
            w_set = {c.lower() for c in w}
            if w_set.issubset(first) or w_set.issubset(second) or w_set.issubset(third):
                res.append(w)
        
        return res