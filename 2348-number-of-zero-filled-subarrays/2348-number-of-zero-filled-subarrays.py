class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = zeros = 0

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                zeros = 0
            
            res += zeros
        
        return res