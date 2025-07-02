class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        hashset = set()
        for i in range(26):
            hashset.add(chr(ord('a') + i))
        
        for ch in sentence:
            if ch in hashset:
                hashset.remove(ch)
            
        return not hashset