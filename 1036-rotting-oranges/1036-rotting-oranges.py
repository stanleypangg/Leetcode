class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        # Find all rotten oranges
        # O(m * n)
        fresh_count = 0
        rotten = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        time = -1
        while rotten:
            time += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        rotten.append((new_r, new_c))
                        fresh_count -= 1
        
        if fresh_count == 0:
            return time
        else:
            return -1