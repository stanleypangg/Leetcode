class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Read the QUESTION
        hashset = set(nums)
        res = 0

        for n in hashset:
            if n - 1 not in hashset:
                length = 0
                while n + length in hashset:
                    length += 1
                res = max(res, length)
        
        return res