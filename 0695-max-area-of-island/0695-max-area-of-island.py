class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            
            self.area += 1
            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        self.area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    self.area = 0
                    dfs(r, c)
                    res = max(res, self.area)   
        return res