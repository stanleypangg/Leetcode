class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxx = minn = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            maxx, minn = max(curr, curr * minn, curr * maxx), min(curr, curr * minn, curr * maxx)
            res = max(res, maxx)

        return res