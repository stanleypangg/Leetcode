class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitalized = word[0].isupper()

        for i in range(1, len(word)):
            if i == 1 and capitalized:
                remainder_capitalized = word[i].isupper()
            elif capitalized and (remainder_capitalized and word[i].islower()):
                return False
            elif capitalized and (not remainder_capitalized and word[i].isupper()):
                return False
            elif not capitalized and word[i].isupper():
                return False
        
        return True