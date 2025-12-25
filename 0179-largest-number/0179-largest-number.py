class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=lambda x: x*10, reverse=True)

        # edge case for trailing zeroes
        if nums[0] == '0':
            return '0'

        return ''.join(nums)