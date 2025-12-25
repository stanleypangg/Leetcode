class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # return > 0
        res = 1
        total = 0

        for n in nums:
            total += n
            res = max(res, 1 - total)
        
        return res