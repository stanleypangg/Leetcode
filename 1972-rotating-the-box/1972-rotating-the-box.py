class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [['.'] * m for _ in range(n)]

        for idx, row in enumerate(boxGrid):
            r = n - 1
            for l in range(n - 1, -1, -1):
                # LI: between l and r there is no obstacle
                if row[l] == '#':
                    res[r][m - idx - 1] = '#'
                    r -= 1
                elif row[l] == '*':
                    res[l][m - idx - 1] = '*'
                    r = l - 1

        return res