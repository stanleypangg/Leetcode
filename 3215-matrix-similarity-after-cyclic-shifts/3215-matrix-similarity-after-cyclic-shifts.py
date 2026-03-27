class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        r = k % n

        idx = 0
        while idx < m:
            row = mat[idx][r:] + mat[idx][:r]
            if row != mat[idx]:
                return False
            idx += 1

            if idx >= m:
                break
            
            row = mat[idx][n - r:] + mat[idx][:n - r]
            if row != mat[idx]:
                return False
            idx += 1
        
        return True