class Solution:
    def rob(self, nums: List[int]) -> int:
        # intuition for circular array?
        # two pass?
        def house_rob(nums):
            one = two = 0
            for n in nums:
                sub = max(one, two + n)
                one, two = sub, one
            return one

        return max(house_rob(nums[:-1]), house_rob(nums[1:]), nums[0])