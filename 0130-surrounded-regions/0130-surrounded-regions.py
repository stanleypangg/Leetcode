class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        self.visited = set()
        self.directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def find_region(r, c):
            region = set()
            region.add((r, c))
            q = deque()
            q.append((r, c))
            is_surrounded = True
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                        is_surrounded = False
                    for dr, dc in self.directions:
                        new_r, new_c = r + dr, c + dc
                        if (0 <= new_r < m and 0 <= new_c < n 
                                and board[new_r][new_c] == "O" and (new_r, new_c) not in self.visited):
                            q.append((new_r, new_c))
                            region.add((new_r, new_c))
                        self.visited.add((new_r, new_c))
            return region, is_surrounded

        for r in range(m):
            for c in range(n):
                if (r, c) in self.visited:
                    continue
                if board[r][c] == 'O':
                    region, is_surrounded = find_region(r, c)
                    if is_surrounded:
                        for region_r, region_c in region:
                            board[region_r][region_c] = "X"