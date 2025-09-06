class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        has_vowel = has_consonant = False

        for c in word:
            if not c.isalnum():
                return False
            
            has_vowel = has_vowel or c.lower() in vowels
            has_consonant = has_consonant or c.lower() in consonants
        
        return has_vowel and has_consonant