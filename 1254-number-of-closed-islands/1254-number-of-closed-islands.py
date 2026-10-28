class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # a closed islands have no cells at the boundary
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = 1
            closed = (0 < r < m - 1) and (0 < c < n - 1)
            for dr, dc in ((1, 0), (0, -1), (-1, 0), (0, 1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 1:
                    continue
                
                closed &= dfs(nr, nc)
            
            return closed
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    res += bool(dfs(r, c))
        return res