class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # commands: sequence of moves it needs to execute
        # 3 types of "moves":
        # -2 -> turn left 90 (counter-clockwise)
        # =1 -> turn right 90 (clockwise)
        # 1 <= k <= 9: move forward k units, one unit at a time

        # obstacles[i] = (xi, yi)

        # return: max squared euclidean distance sqrt((x1 - x0)^2 + (y1 - y0)^2) at any point
        res = 0
        x = y = 0

        # N = 0, E = 1, S = 2, W = 3
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        facing = 0 # index 0 = North

        obstacles = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:
                facing = (facing - 1) % 4
            elif command == -1:
                facing = (facing + 1) % 4
            else:
                # just loop k tiems?
                dx, dy = directions[facing]
                for _ in range(command):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    res = max(res, x ** 2 + y ** 2)
        
        return res