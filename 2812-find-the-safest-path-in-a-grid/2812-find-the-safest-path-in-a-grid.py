class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
        
        def out_of_bounds(r, c):
            return r < 0 or r >= n or c < 0 or c >= n

        safety = []
        q = deque()
        for r in range(n):
            safety.append([])

            for c in range(n):
                if grid[r][c] == 1:
                    # cur_r, cur_c, thief_r, thief_c
                    safety[r].append(0)
                    q.append((r, c))
                else:
                    safety[r].append(None)
        
        max_safety = float('-inf')
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if out_of_bounds(nr, nc) or safety[nr][nc] is not None:
                    continue
                
                safety[nr][nc] = safety[r][c] + 1
                max_safety = max(max_safety, safety[nr][nc])
                q.append((nr, nc))
            
        def connected(cur_safety):
            if safety[0][0] < cur_safety or safety[n - 1][n - 1] < cur_safety:
                return False
            
            q = deque([(0, 0)])
            visited = {(0, 0)}

            while q:
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if out_of_bounds(nr, nc) or (nr, nc) in visited or safety[nr][nc] < cur_safety:
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
            
            return False

        l, r = 0, max_safety
        while l < r:
            mid = (l + r + 1) // 2
            if connected(mid):
                l = mid
            else:
                r = mid - 1
        
        return l