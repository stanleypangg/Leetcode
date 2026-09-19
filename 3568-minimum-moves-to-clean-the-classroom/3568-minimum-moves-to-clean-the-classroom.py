class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None

        for r in range(m):
            for c in range(n):
                cur = classroom[r][c]
                if cur == 'S':
                    start = (r, c)
                elif cur == 'L':
                    litter[(r, c)] = len(litter)
        
        moves = 0
        q = deque()
        q.append((*start, energy, 0)) # (r, c, energy, bitmask)

        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        visited = {}
        visited[(*start, 0)] = energy # (r, c, bitmask) -> max energy

        while q:
            for _ in range(len(q)):
                r, c, e, b = q.popleft()

                # check if all cleaned
                target = (1 << len(litter)) - 1
                if (b & target) == target:
                    return moves
                
                # no energy
                if e == 0:
                    continue

                # check neighbours
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    ne = e - 1
                    nb = b

                    # out of bounds
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    nextt = classroom[nr][nc]
                    if nextt == 'L':
                        pos = litter[(nr, nc)]
                        nb |= (1 << pos)
                    elif nextt == 'X':
                        continue
                    elif nextt == 'R':
                        ne = energy

                    key = (nr, nc, nb)
                    if visited.get(key, -1) >= ne:
                        continue

                    visited[key] = ne
                    q.append((nr, nc, ne, nb))
            
            moves += 1
        
        return -1 