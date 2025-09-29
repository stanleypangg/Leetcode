class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        def lte(word1, word2):
            # True if word1 <= word2
            i = 0
            while i < len(word1) and i < len(word2):
                char1, char2 = word1[i], word2[i]
                if order_map[char1] > order_map[char2]:
                    return False
                elif order_map[char1] < order_map[char2]:
                    return True
                i += 1
            
            return len(word1) <= len(word2)
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if not lte(word1, word2):
                return False
        return True