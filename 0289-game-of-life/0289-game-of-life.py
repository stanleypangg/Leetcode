class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        adjacent_directions = (
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, 1), (-1, -1), (1, -1)
        )

        for r in range(m):
            for c in range(n):
                live_neighbors = 0

                for dr, dc in adjacent_directions:
                    nr = r + dr
                    nc = c + dc

                    # check if in range
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    
                    # check initial state
                    if board[nr][nc] == 1 or board[nr][nc] == 2:
                        live_neighbors += 1
                
                if board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 3 # dead to alive
                else:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2 # alive to dead
    
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1