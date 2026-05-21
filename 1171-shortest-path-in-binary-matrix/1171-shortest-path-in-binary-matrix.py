class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] == 1:
            return -1
        if m == 1 and n == 1:
            return 1
        

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
        best = {}
        best[(0, 0)] = 1
        q = deque([(0, 0, 1)])

        while q:
            r, c, length = q.popleft()
            if r == m - 1 and c == n - 1:
                return length
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                n_length = length + 1
                
                out_of_bounds = nr < 0 or nr >= m or nc < 0 or nc >= n
                if out_of_bounds:
                    continue
                
                blocked = grid[nr][nc] == 1
                not_better = n_length >= best.get((nr, nc), float('inf'))
                if blocked or not_better:
                    continue
                
                q.append((nr, nc, n_length))
                best[(nr, nc)] = n_length
        
        return -1