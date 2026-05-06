class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        # f(0)
        prev = res = sum(i * n for i, n in enumerate(nums))

        for i in range(len(nums) - 1):
            cur = prev - total + n * nums[i]
            res = max(res, cur)
            prev = cur
        
        return res