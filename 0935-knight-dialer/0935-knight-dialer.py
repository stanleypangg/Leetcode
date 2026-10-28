class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        jump = [
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (0, 3, 9),
            (),
            (0, 1, 7),
            (2, 6),
            (1, 3),
            (2, 4)
        ]

        for _ in range(1, n):
            dp = [
                sum(dp[nei] for nei in jump[num]) 
                for num 
                in range(10)
            ]
        
        return sum(dp) % 1_000_000_007