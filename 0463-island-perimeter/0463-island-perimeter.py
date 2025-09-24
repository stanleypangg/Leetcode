class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for r in range(m):
            for c in range(n):
                # land
                if grid[r][c] == 1:
                    res += 4
                    # land below
                    if r + 1 < m and grid[r + 1][c] == 1:
                        res -= 2
                    # land to right
                    if c + 1 < n and grid[r][c + 1] == 1:
                        res -= 2
        
        return res