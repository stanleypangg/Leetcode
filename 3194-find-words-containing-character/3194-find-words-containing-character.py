class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # O(nw), w = max(word for word in words)
        return [i for i in range(len(words)) if x in words[i]]