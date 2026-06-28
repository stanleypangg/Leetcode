class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def in_bounds(r, c):
            return r >= 0 and r < 8 and c >= 0 and c < 8

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
        opposite = {'B': 'W', 'W': 'B'}

        for dr, dc in dirs:
            # check to see if direct next is oppposite
            nr, nc = rMove + dr, cMove + dc
            if not in_bounds(nr, nc) or board[nr][nc] != opposite[color]:
                continue
            
            # now need to find next endpoint, which is same as color
            while in_bounds(nr, nc) and board[nr][nc] == opposite[color]:
                nr += dr
                nc += dc
            
            # we've found the end point, if its still in bounds and is color
            if in_bounds(nr, nc) and board[nr][nc] == color:
                return True
        
        return False