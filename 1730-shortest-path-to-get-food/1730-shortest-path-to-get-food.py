class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        start = None
        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                if cur == '*':
                    grid[r][c] = 'X'
                    start = (r, c)
                    break            
            if start is not None:
                break

        length = 0
        q = deque()
        q.append(start)

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                cur = grid[r][c]
                if cur == '#':
                    return length
                
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 'X':
                        continue

                    if grid[nr][nc] == '#':
                        return length + 1

                    grid[nr][nc] = 'X'
                    q.append((nr, nc))

            length += 1
        
        return -1