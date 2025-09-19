class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        total = 0
        m, n = len(board), len(board[0])

        # dfs right and down upon first appearance
        def dfs(r, c, dr, dc):
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'X':
                board[r][c] = '.'
                dfs(r + dr, c + dc, dr, dc)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    dfs(r, c, 1, 0)
                    board[r][c] = 'X'
                    dfs(r, c, 0, 1)
                    total += 1
        
        return total