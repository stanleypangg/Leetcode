class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        res = 0
        m, n = len(room), len(room[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) # RDLU
        rooms = set()
        states = set()

        cur = (0, 0, 0)
        while cur not in states:
            states.add(cur)
            r, c, direction = cur

            if (r, c) not in rooms:
                res += 1
                rooms.add((r, c))

            rotations = 0

            for _ in range(4):
                dr, dc = dirs[direction]
                nr = r + dr
                nc = c + dc

                # now check if valid
                if nr >= 0 and nr < m and nc >= 0 and nc < n and room[nr][nc] == 0:
                    break

                direction = (direction + 1) % 4
                rotations += 1
        
            if rotations == 4:
                return res
            
            cur = (nr, nc, direction)

        return res