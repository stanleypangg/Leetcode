class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combo = []

        def bt(i):
            if len(combo) == k:
                res.append(combo.copy())
                return
            
            for num in range(i, n + 1):
                combo.append(num)
                bt(num + 1)
                combo.pop()
        
        bt(1)
        return res