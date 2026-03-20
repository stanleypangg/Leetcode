class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        res = [[-1] * (n - k + 1) for _ in range(m - k + 1)]
        
        for sr in range(m - k + 1):
            for sc in range(n - k + 1):
                window = {
                    grid[r][c] 
                    for r in range(sr, sr + k) for c in range(sc, sc + k)
                }
                window = sorted(list(window))

                closest = float('inf')
                
                for i in range(1, len(window)):
                    closest = min(closest, abs(window[i] - window[i - 1]))
                
                res[sr][sc] = closest if closest != float('inf') else 0
        
        return res