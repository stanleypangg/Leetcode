class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key insight: for current num, if num - 1 not in nums, its a start of a sequence

        if not nums:
            return 0
        
        res = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue
            
            # start of sequence
            length = 1
            while num + 1 in nums:
                length += 1
                num += 1
            
            res = max(res, length)
        
        return res