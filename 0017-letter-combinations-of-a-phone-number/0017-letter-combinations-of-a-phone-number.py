class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs', 
            '8': 'tuv',
            '9': 'wxyz'
        }

        self.res = []

        def bt(curr, i):
            if i >= len(digits):
                self.res.append(curr)
                return
            
            num_to_digit = mapping[digits[i]]
            for num in num_to_digit:
                bt(curr + num, i + 1)
            
        bt("", 0)
        return self.res