class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        fresh_count = 0

        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                if cur == 1:
                    fresh_count += 1
                elif cur == 2:
                    q.append((r, c))
        
        if fresh_count == 0:
            return 0

        minutes = -1
        while q:
            minutes += 1

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nei_r = r + dr
                    nei_c = c + dc 

                    if nei_r < 0 or nei_r >= m or nei_c < 0 or nei_c >= n:
                        continue
                    
                    if grid[nei_r][nei_c] == 1:
                        q.append((nei_r, nei_c))
                        grid[nei_r][nei_c] = 2
                        fresh_count -= 1
        
        if fresh_count > 0:
            return -1

        return minutes