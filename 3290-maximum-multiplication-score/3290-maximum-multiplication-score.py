class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # a.size == 4, b.size >= 4
        # choose 4 indices from b s.t. they r strictly increasing
        # multiply them in respective order of elemnts of a
        # return max mult score

        n = len(b)
        # dp[a][b] = max mult score for i_a at index b
        dp = [[float('-inf')] * (n + 1) for _ in range(5)]
        dp[4] = [0] * (n + 1)

        for i in range(3, -1, -1):
            for j in range(n - 4 + i, i - 1, -1):
                curr_score = a[i] * b[j] + dp[i + 1][j + 1] if dp[i + 1][j + 1] != float('-inf') else 0
                dp[i][j] = max(curr_score, dp[i][j + 1])


        return dp[0][0]