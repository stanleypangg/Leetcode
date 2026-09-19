class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[None] * n for _ in range(n)]

        facing = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bounds = [n - 1, n - 1, 0, 0]

        r = c = 0
        for i in range(1, n ** 2 + 1):
            res[r][c] = i

            # try moving in current direction
            dr, dc = dirs[facing]
            nr, nc = r + dr, c + dc
            right, bottom, left, top = bounds

            if top <= nr <= bottom and left <= nc <= right: # in bounds! continue:
                r, c = nr, nc
                continue
            
            # now we are out of bounds
            # change direciton, facing, and close gap in bounds
            facing = (facing + 1) % 4
            dr, dc = dirs[facing]
            r, c = r + dr, c + dc

            # close gap behind
            behind = (facing - 2) % 4
            if 0 <= behind <= 1:
                bounds[behind] -= 1
            else:
                bounds[behind] += 1
        
        return res