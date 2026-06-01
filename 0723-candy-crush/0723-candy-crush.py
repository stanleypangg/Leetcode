class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        def crush():
            # do rows first
            has_crush = False

            for row in range(m):
                l = 0
                for r in range(n + 1):
                    if r == n or abs(board[row][l]) != abs(board[row][r]):
                        if r - l >= 3 and board[row][l] != 0:
                            has_crush = True
                            for c in range(l, r):
                                board[row][c] = -abs(board[row][l])
                        l = r
                        
            
            for col in range(n):
                u = 0
                for d in range(m + 1):
                    if d == m or abs(board[u][col]) != abs(board[d][col]):
                        if d - u >= 3 and board[u][col] != 0:
                            has_crush = True
                            for r in range(u, d):
                                board[r][col] = -abs(board[u][col])
                        u = d

            return has_crush
            
        def gravity():
            for col in range(n):
                fall = 0
                for row in range(m - 1, -1, -1):
                    if board[row][col] < 0:
                        board[row][col] = 0
                        fall += 1
                    else:
                        board[row][col], board[row + fall][col] = 0, board[row][col]
        
        while crush():
            gravity()
        
        return board