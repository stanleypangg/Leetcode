class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        # dp[i] = (max subarray, min subarray) both including i
        dp = [float('-inf')] * len(nums)
        dp[0] = (res, res)

        for i in range(1, len(nums)):
            prev_max, prev_min = dp[i - 1]
            curr = nums[i]

            curr_max = max(curr, curr * prev_max, curr * prev_min)
            curr_min = min(curr, curr * prev_max, curr * prev_min)
            dp[i] = (curr_max, curr_min)

            res = max(res, curr_max)

        return res