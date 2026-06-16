class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''

        for word in words:
            weight = 0
            for char in word:
                idx = ord(char) - ord('a')
                weight += weights[idx]
            
            weight %= 26
            mapped_ord = ord('z') - weight

            res += chr(mapped_ord)
        
        return res