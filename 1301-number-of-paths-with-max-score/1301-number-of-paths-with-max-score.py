class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dirs = ((0, 1), (1, 0), (1, 1))
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n][n] = [0, 1]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                cur = board[r][c]
                if cur == 'X':
                    continue
                
                cur_score = int(cur) if cur.isdigit() else 0
                prev = {}
                for dr, dc in dirs:
                    score, num_paths = dp[r + dr][c + dc]
                    prev[score] = prev.get(score, 0) + num_paths
                
                max_score = max(prev)
                dp[r][c] = [max_score + cur_score, prev[max_score]]
        
        if dp[0][0][1] == 0:
            return [0, 0]
        else:
            MODULO = 10 ** 9 + 7
            max_score, num_paths = dp[0][0]
            return [max_score, num_paths % MODULO]