class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        # naive, iterate guards, scan all spots
        # O(gwmn)

        # G, W, B, O
        grid = [['O'] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 'W'
        for r, c in guards:
            grid[r][c] = 'G'
        
        for r, c in guards:
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                steps = 1
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in {'W', 'G'}:
                    grid[nr][nc] = 'B'
                    nr += dr
                    nc += dc
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'O':
                    res += 1
        
        return res