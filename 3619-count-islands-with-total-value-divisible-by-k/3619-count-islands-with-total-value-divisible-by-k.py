class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            total = grid[r][c]
            grid[r][c] = 0

            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                    continue
                total += dfs(nr, nc)
            
            return total
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    res += bool(dfs(r, c) % k == 0)
        
        return res