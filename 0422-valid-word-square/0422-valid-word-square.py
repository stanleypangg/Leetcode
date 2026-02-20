class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            if word != ''.join(w[i] for w in words if i < len(w)):
                return False
        return True