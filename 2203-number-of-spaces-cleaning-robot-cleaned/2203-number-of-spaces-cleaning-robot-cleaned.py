class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) # RDLU
        rooms = set()
        states = set()

        r = c = direction = 0
        while (r, c, direction) not in states:
            states.add((r, c, direction))
            rooms.add((r, c))

            rotations = 0

            for _ in range(4):
                dr, dc = dirs[direction]
                nr, nc = r + dr, c + dc

                # now check if valid
                if nr >= 0 and nr < m and nc >= 0 and nc < n and room[nr][nc] == 0:
                    r, c = nr, nc
                    break

                direction = (direction + 1) % 4
            else:
                break
            
        return len(rooms)