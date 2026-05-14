class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            # first check if its even reached
            if dp[i] == -1:
                continue

            for j in range(i + 1, n):
                # check if you can jump there
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
                
        return -1 if dp[n - 1] == -1 else dp[n - 1]