class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq_a = [0] * (n + 1)
        freq_b = [0] * (n + 1)
        res = [0] * n

        prefix = 0
        for i, (a, b) in enumerate(zip(A, B)):
            freq_a[a] = freq_b[b] = 1
            
            if a == b:
                prefix += 1
            else:
                prefix += freq_a[b] + freq_b[a]
            
            res[i] = prefix
        
        return res