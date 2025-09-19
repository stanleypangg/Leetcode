class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        total = 0
        m, n = len(board), len(board[0])
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    # we only ever explore right and down, if we see an 'X' up or left, it's already been explored
                    if (r > 0 and board[r - 1][c] == 'X') or (c > 0 and board[r][c - 1] == 'X'):
                        continue
                    # only count the top left of the battleship 
                    total += 1
        
        return total