class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        best = {}
        best[(0, 0)] = k
        q = deque([(0, 0, k)])
        depth = 0

        while q:
            for _ in range(len(q)):
                r, c, elim_left = q.popleft()
                if r == m - 1 and c == n - 1:
                    return depth

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    
                    # valid atp
                    n_elim_left = elim_left
                    if grid[nr][nc] == 1:
                        n_elim_left -= 1
                    
                    # can't enter obs, or we've have a better position here
                    if n_elim_left < 0 or n_elim_left <= best.get((nr, nc), -1):
                        continue
                    
                    q.append((nr, nc, n_elim_left))
                    best[(nr, nc)] = n_elim_left
            
            depth += 1
        
        return -1