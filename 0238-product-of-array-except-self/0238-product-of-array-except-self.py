class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)

        prefix = nums[0]
        for i in range(1, len(nums)):
            ret[i] *= prefix
            prefix *= nums[i]
        
        postfix = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]
        
        return ret