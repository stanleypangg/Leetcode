class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        INF = 2 ** 31 - 1
        dirs = ((0, 1), (-1, 0), (0, -1), (1, 0))

        # multi source bfs
        q = deque()
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or rooms[nr][nc] != INF:
                        continue
                    
                    rooms[nr][nc] = depth
                    q.append((nr, nc))