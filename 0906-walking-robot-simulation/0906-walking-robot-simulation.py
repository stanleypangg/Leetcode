class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(tuple(obs) for obs in obstacles)
        res = x = y = cur_dir = 0 # N = 0, E = 1, S = 2, W = 3

        dir_map = ((0, 1), (1, 0), (0, -1), (-1, 0))

        res = 0

        for c in commands:
            if c == -2:
                cur_dir = (cur_dir - 1) % 4
            elif c == -1:
                cur_dir = (cur_dir + 1) % 4
            else:
                dx, dy = dir_map[cur_dir]
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    res = max(res, x ** 2 + y ** 2)
        
        return res