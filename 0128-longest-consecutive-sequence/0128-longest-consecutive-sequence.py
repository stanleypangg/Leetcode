class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if not num - 1 in num_set:
                seq_count = 1
                while num + seq_count in num_set:
                    seq_count += 1
                longest = max(longest, seq_count)
        
        return longest