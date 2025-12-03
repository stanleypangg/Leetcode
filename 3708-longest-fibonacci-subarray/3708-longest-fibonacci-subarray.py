class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = curr_len = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                curr_len += 1
                res = max(res, curr_len)
            else:
                curr_len = 2
        return res