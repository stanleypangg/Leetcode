class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        if grid[0][0] == 1:
            health -= 1
            
        visited = {(0, 0): health}
        q = deque([(0, 0, health)])

        while q:
            r, c, h = q.popleft()
            if (r, c) == (m - 1, n - 1):
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                nh = h - grid[nr][nc]
                if nh <= 0 or nh <= visited.get((nr, nc), 0):
                    continue

                visited[(nr, nc)] = nh
                q.append((nr, nc, nh))
        
        return False