class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = cur_max = cur_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')

        for n in nums:
            cur_max = max(cur_max + n, n)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + n, n)
            min_sum = min(cur_min, min_sum)
            total += n
        
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum