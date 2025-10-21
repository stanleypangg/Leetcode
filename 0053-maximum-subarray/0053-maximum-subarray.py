class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(0, curr_sum) + num
            res = max(res, curr_sum)
        
        return res