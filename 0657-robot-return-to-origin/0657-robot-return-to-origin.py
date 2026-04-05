class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        dirs = {'U': (0, 1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, -1)}

        for m in moves:
            dx, dy = dirs[m]
            x += dx
            y += dy
        
        return x == y == 0