class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [0] + [-inf] * 4

        for b_i in b:
            for j in range(3, -1, -1):
                dp[j + 1] = max(dp[j + 1], dp[j] + a[j] * b_i)

        return dp[4]