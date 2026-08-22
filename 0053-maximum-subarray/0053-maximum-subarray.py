class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_total = 0
        max_total = float('-inf')

        for n in nums:
            if cur_total < 0:
                cur_total = 0
            
            cur_total += n
            max_total = max(max_total, cur_total)
        
        return max_total