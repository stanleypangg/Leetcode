class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] = number of jumps to get to pos i
        n = len(nums)
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        j = 1
        for i in range(len(nums)):
            while j <= min(i + nums[i], n - 1):
                dp[j] = dp[i] + 1
                j += 1
                
            if j == n:
                break

        return dp[-1]