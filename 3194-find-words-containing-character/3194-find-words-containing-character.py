class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # O(nw), w = max(word for word in words)
        res = []
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res