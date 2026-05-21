class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        k = 0
        start = None

        # first pass to find @ and k
        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                if cur == '@':
                    start = (r, c)
                elif cur.isalpha():
                    k = max(k, ord(cur.lower()) - ord('a') + 1)
        
        # r, c, length, key_state
        # key_state_i = {0, 1}
        # 0 for no key
        # 1 for has key
        visited = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        init_state = (start[0], start[1], 0, (0,) * k)
        q = deque([init_state])

        while q:
            r, c, length, keys = q.popleft()
            if all(k == 1 for k in keys):
                return length
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                out_of_bounds = nr < 0 or nr >= m or nc < 0 or nc >= n
                if out_of_bounds:
                    continue

                cur = grid[nr][nc]
                if cur == '#' or (nr, nc, keys) in visited:
                    continue

                # key / lock state
                n_keys = keys
                if cur.isalpha():
                    key_idx = ord(cur.lower()) - ord('a')
                    if cur.islower():
                        n_keys = list(keys)
                        n_keys[key_idx] = 1
                        n_keys = tuple(n_keys)
                    elif keys[key_idx] == 0:
                        # bumped into lock AND dont have key
                        continue
            
                q.append((nr, nc, length + 1, n_keys))
                visited.add((nr, nc, n_keys))
        
        return -1