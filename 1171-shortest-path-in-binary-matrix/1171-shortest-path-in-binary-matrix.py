class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1
        

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
        visited = set()
        visited.add((0, 0))
        q = deque([(0, 0, 1)])

        while q:
            r, c, length = q.popleft()
            if r == n - 1 and c == n - 1:
                return length
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                n_length = length + 1
                
                out_of_bounds = nr < 0 or nr >= n or nc < 0 or nc >= n
                if out_of_bounds:
                    continue
                
                if grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue
                
                q.append((nr, nc, n_length))
                visited.add((nr, nc))
        
        return -1