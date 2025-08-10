class Solution:
    def rob(self, nums: List[int]) -> int:
        # intuition for circular array?
        # two pass?
        if len(nums) == 1:
            return nums[0]
            
        one = two = 0
        
        for i in range(len(nums) - 1):
            sub = max(one, nums[i] + two)
            one, two = sub, one
        
        res = one

        one = two = 0
        for i in range(1, len(nums)):
            sub = max(one, nums[i] + two)
            one, two = sub, one
        
        return max(res, one)