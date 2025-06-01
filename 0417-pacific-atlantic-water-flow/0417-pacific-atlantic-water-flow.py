class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, prev_height):
            if (
                (r, c) in ocean or
                r < 0 or r == m or
                c < 0 or c == n or
                heights[r][c] < prev_height
            ):
                return
            
            ocean.add((r, c))
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        
        for r in range(m):
            dfs(r, 0, pacific, 0)
            dfs(r, n - 1, atlantic, 0)
        for c in range(n):
            dfs(0, c, pacific, 0)
            dfs(m - 1, c, atlantic, 0)
        
        return [[r, c] for r, c in pacific.intersection(atlantic)]