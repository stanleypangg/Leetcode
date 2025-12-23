class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0: 1}
        total = res = 0
        
        for n in nums:
            total += n

            if total - k in prefixes:
                res += prefixes[total - k]
            
            prefixes[total] = prefixes.get(total, 0) + 1
        
        return res