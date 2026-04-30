class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # how to encode an island and store it in visited
        islands = set()
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(r, c, base_r, base_c, pos):
            grid[r][c] = 0
            pos.add((r - base_r, c - base_c))
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                    continue
                
                dfs(nr, nc, base_r, base_c, pos)
            
            return frozenset(pos)
        
        res = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                
                pos = dfs(r, c, r, c, set())
                if pos in islands:
                    continue
                
                islands.add(pos)
                res += 1
        
        return res