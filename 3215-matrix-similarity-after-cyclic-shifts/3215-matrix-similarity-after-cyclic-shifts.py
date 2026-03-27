class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        r = k % n

        for i in range(m):
            if i % 2 == 0:
                row = mat[i][r:] + mat[i][:r]
            else:
                row = mat[i][n - r:] + mat[i][:n - r]
            
            if row != mat[i]:
                return False
        
        return True