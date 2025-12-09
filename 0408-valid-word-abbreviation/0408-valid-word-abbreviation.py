class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_i = a_i = 0

        while w_i < len(word) and a_i < len(abbr):
            if abbr[a_i].isalpha():
                if abbr[a_i] != word[w_i]:
                    return False
                w_i += 1
                a_i += 1
            else:
                # abbr[w_i] must be numeric
                if abbr[a_i] == '0':
                    return False
                
                number = 0
                while a_i < len(abbr) and abbr[a_i].isdigit():
                    number = number * 10 + int(abbr[a_i])
                    a_i += 1
                w_i += number
        
        return w_i == len(word) and a_i == len(abbr)