class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []

        for i in range(m + n - 1):
            reverse = i % 2 != 0
            if reverse:
                row = max(0, i - n + 1)
                col = min(n - 1, i)
            else:
                row = min(m - 1, i)
                col = max(0, i - m + 1)
            
            sign = -1 if reverse else 1
            
            while 0 <= row < m and 0 <= col < n:
                res.append(mat[row][col])
                row -= sign
                col += sign
            
        return res