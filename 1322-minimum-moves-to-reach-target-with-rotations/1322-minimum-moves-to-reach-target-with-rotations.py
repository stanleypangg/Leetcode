class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # bfs
        # visited state
        # could just be the two snake coords
        
        # how to represent snake
        # snake is two coords
        # if rows equal, its horiz
        # if cols equal, its vert

        def cell_clear(pos):
            return 0 <= pos[0] < n and 0 <= pos[1] < n and grid[pos[0]][pos[1]] == 0
        
        def push(tail, head, length):
            if (tail, head) not in visited:
                visited.add((tail, head))
                q.append((tail, head, length))

        n = len(grid)
        visited = {((0, 0), (0, 1))}
        q = deque([((0, 0), (0, 1), 0)])

        while q:
            tail, head, length = q.popleft()
            if tail == (n - 1, n - 2) and head == (n - 1, n - 1):
                return length
            
            tail_r, tail_c = tail
            head_r, head_c = head
            
            # move right / move down
            for dr, dc in ((0, 1), (1, 0)):
                n_tail = (tail_r + dr, tail_c + dc)
                n_head = (head_r + dr, head_c + dc)
                if cell_clear(n_tail) and cell_clear(n_head):
                    push(n_tail, n_head, length + 1)
            
            # if horizontal, attempt rotate clockwise
            if tail_r == head_r:
                n_head = (tail_r + 1, tail_c)
                if cell_clear(n_head) and cell_clear((head_r + 1, head_c)):
                    push(tail, n_head, length + 1)
            else:
                n_head = (tail_r, tail_c + 1)
                if cell_clear(n_head) and cell_clear((head_r, head_c + 1)):
                    push(tail, n_head, length + 1)
        
        return -1