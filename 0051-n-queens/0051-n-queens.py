class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q' or abs(row - i) == abs(col - board[i].index('Q')):
                    return False
            return True

        def bt(board, row):
            # Base case
            if row == n:
                res.append([''.join(row) for row in board])
                return

            for col in range (n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    bt(board, row + 1)
                    board[row][col] = '.'
        
        bt([['.' for _ in range(n)] for _ in range(n)], 0)
        return res