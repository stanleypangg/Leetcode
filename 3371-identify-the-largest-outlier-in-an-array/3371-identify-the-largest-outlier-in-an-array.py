class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        freq = {}
        total = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            total += num
        
        res = float('-inf')
        for x, count in freq.items():
            if x <= res:
                continue
            if (total - x) % 2 == 1:
                continue
                
            special_sum = (total - x) // 2
            if special_sum in freq and (special_sum != x or freq[x] >= 2):
                res = max(res, x)
        
        return res