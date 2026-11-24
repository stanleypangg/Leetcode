class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        res = sum(technique2)
        
        diff = [t1 - t2 for t1, t2 in zip(technique1, technique2)]
        diff.sort(reverse=True)
        for i, val in enumerate(diff):
            if i < k or val > 0:
                res += val
            else:
                break
        
        return res